from lxml import etree
from urllib.parse import urlparse
from celery.utils.log import get_logger

from . import detchar
from . import gcn
from . import gracedb
from . import external_skymaps
from . import lvalert
from . import raven

log = get_logger(__name__)


@gcn.handler(gcn.NoticeType.SNEWS,
             queue='exttrig',
             shared=False)
def handle_snews_gcn(payload):
    """Handles the payload from SNEWS alerts.

    Prepares the alert to be sent to graceDB as 'E' events.
    """
    root = etree.fromstring(payload)

    #  Get TrigID and Test Event Boolean
    trig_id = root.find("./What/Param[@name='TrigID']").attrib['value']
    test_event = root.find("./What/Group[@name='Trigger_ID']" +
                           "/Param[@name='Test']").attrib['value']

    event_observatory = 'SNEWS'
    query = 'group: External pipeline: {} grbevent.trigger_id = "{}"'.format(
        event_observatory, trig_id)
    events = gracedb.get_events(query=query)

    if events:
        assert len(events) == 1, 'Found more than one matching GraceDB entry'
        event, = events
        graceid = event['graceid']
        gracedb.replace_event(graceid, payload)
        return

    elif test_event == 'true':
        graceid = gracedb.create_event(filecontents=payload,
                                       search='Supernova',
                                       group='Test',
                                       pipeline=event_observatory)

    else:
        graceid = gracedb.create_event(filecontents=payload,
                                       search='Supernova',
                                       group='External',
                                       pipeline=event_observatory)
    event = gracedb.get_event(graceid)
    start, end = event['gpstime'], event['gpstime']
    # Pre-start and post-end padding is applied by check_vectors
    detchar.check_vectors(event, event['graceid'], start, end)


@gcn.handler(gcn.NoticeType.FERMI_GBM_FLT_POS,
             gcn.NoticeType.FERMI_GBM_GND_POS,
             gcn.NoticeType.FERMI_GBM_FIN_POS,
             gcn.NoticeType.SWIFT_BAT_GRB_POS_ACK,
             gcn.NoticeType.FERMI_GBM_SUBTHRESH,
             queue='exttrig',
             shared=False)
def handle_grb_gcn(payload):
    """Handles the payload from Fermi and Swift alerts.

    Prepares the alert to be sent to graceDB as 'E' events.
    """
    root = etree.fromstring(payload)
    u = urlparse(root.attrib['ivorn'])
    stream_path = u.path

    #  Get TrigID
    try:
        trig_id = root.find("./What/Param[@name='TrigID']").attrib['value']
    except AttributeError:
        trig_id = root.find("./What/Param[@name='Trans_Num']").attrib['value']

    stream_obsv_dict = {'/SWIFT': 'Swift',
                        '/Fermi': 'Fermi'}
    event_observatory = stream_obsv_dict[stream_path]

    reliability = root.find("./What/Param[@name='Reliability']")
    if reliability is not None and int(reliability.attrib['value']) <= 4:
        return

    ivorn = root.attrib['ivorn']
    if 'subthresh' in ivorn.lower():
        search = 'SubGRB'
    else:
        search = 'GRB'

    query = 'group: External pipeline: {} grbevent.trigger_id = "{}"'.format(
        event_observatory, trig_id)
    events = gracedb.get_events(query=query)

    if events:
        assert len(events) == 1, 'Found more than one matching GraceDB entry'
        event, = events
        graceid = event['graceid']
        gracedb.replace_event(graceid, payload)
        event = gracedb.get_event(graceid)

    else:
        graceid = gracedb.create_event(filecontents=payload,
                                       search=search,
                                       group='External',
                                       pipeline=event_observatory)
        event = gracedb.get_event(graceid)
        start = event['gpstime']
        end = start + event['extra_attributes']['GRB']['trigger_duration']
        detchar.check_vectors(event, event['graceid'], start, end)

    external_skymaps.create_upload_external_skymap(event)
    if event['pipeline'] == 'Fermi':
        external_skymaps.get_upload_external_skymap(graceid)


@lvalert.handler('superevent',
                 'mdc_superevent',
                 'external_fermi',
                 'external_swift',
                 shared=False)
def handle_grb_lvalert(alert):
    """Parse an LVAlert message related to superevents/GRB external triggers
    and dispatch it to other tasks.

    Notes
    -----
    This LVAlert message handler is triggered by creating a new superevent or
    GRB external trigger event, or applying the ``EM_COINC`` label to any
    superevent:

    * Any new event triggers a coincidence search with
      :meth:`gwcelery.tasks.raven.coincidence_search`.
    * The ``EM_COINC`` label triggers the creation of a combined GW-GRB sky map
      using :meth:`gwcelery.tasks.external_skymaps.create_combined_skymap`.

    """
    # Determine GraceDB ID
    graceid = alert['uid']

    if alert['alert_type'] == 'new' and \
            alert['object'].get('group') == 'External':
        raven.coincidence_search(graceid, alert['object'], group='CBC')
        raven.coincidence_search(graceid, alert['object'],
                                 group='Burst')
    elif 'S' in graceid:
        preferred_event_id = gracedb.get_superevent(graceid)['preferred_event']
        group = gracedb.get_event(preferred_event_id)['group']
        if alert['alert_type'] == 'new':
            raven.coincidence_search(graceid, alert['object'],
                                     group=group,
                                     pipelines=['Fermi', 'Swift'])


@lvalert.handler('superevent',
                 'mdc_superevent',
                 'external_snews',
                 shared=False)
def handle_snews_lvalert(alert):
    """Parse an LVAlert message related to superevents/SN external triggers and
    dispatch it to other tasks.

    Notes
    -----
    This LVAlert message handler is triggered by creating a new superevent or
    SN external trigger event, or applying the ``EM_COINC`` label to any
    superevent:

    * Any new event triggers a coincidence search with
      :meth:`gwcelery.tasks.raven.coincidence_search`.

    """
    # Determine GraceDB ID
    graceid = alert['uid']

    if alert['object'].get('group', '') == 'Test':
        pass
    elif alert['alert_type'] == 'new' and \
            alert['object'].get('group') == 'External':
        raven.coincidence_search(graceid, alert['object'],
                                 group='Burst', pipelines=['SNEWS'])
    elif 'S' in graceid:
        preferred_event_id = gracedb.get_superevent(graceid)['preferred_event']
        group = gracedb.get_event(preferred_event_id)['group']
        if alert['alert_type'] == 'new' and group == 'Burst':
            raven.coincidence_search(graceid, alert['object'],
                                     group=group, pipelines=['SNEWS'])
