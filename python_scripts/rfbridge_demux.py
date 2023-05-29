d = { '1':['motion_toilet_upstairs','ON','true'],
      '2':['sensor_doorbell','ON','true'],
      '3':['motion_toilet_downstairs','ON','true'],
      '4':['motion_hallway_2','ON','true'],
      '5':['motion_hallway_0','ON','true'],
      '6':['motion_garage','ON','true'],
    }

myPayload = data.get('payload', {})
myRFMessageKey = str(myPayload.get('payload_json').get('RfReceived').get('RfKey'))

if myRFMessageKey is not None:
  if myRFMessageKey in d.keys():
    service_data = {'topic':'home/{}'.format(d[myRFMessageKey][0]), 'payload':'{}'.format(d[myRFMessageKey][1]), 'qos':0, 'retain':'{}'.format(d[myRFMessageKey][2])}
  else:
    service_data = {'topic':'home/unknown', 'payload':'{}'.format(myPayload), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(myRFMessageKey))
  hass.services.call('mqtt', 'publish', service_data, False)