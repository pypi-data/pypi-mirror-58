import paho.mqtt.publish as mqttpublish
import logging

class Cayenne:
    def __init__(self, host, username, password, clientId):
        self._host = host
        self._username = username
        self._password = password
        self._clientId = clientId

    def publish(self, sensors, sensor_mapping, qos):
        msgs = list()
        # for for topic is "v1/username/things/clientid/data/1" #replace username and clientid here and increment last digit for every sensor
        topic_root = "v1/{}/things/{}/data/".format(self._username, self._clientId)
        for sensor in sensors:
            conf = sensor_mapping.get(sensor.identifier)
            cayennetemp     = "temp,c={}".format(sensor.temperature)
            cayennehumidity = "rel_hum,p={}".format(sensor.humidity)
            msgs.append((topic_root + conf['tempchannel'], cayennetemp,     qos, True))
            msgs.append((topic_root + conf['humchannel'],  cayennehumidity, qos, True))
        try:
            logging.debug("Publishing %s messages", len(msgs))
            logging.debug(msgs)
            mqttpublish.multiple(msgs, hostname=self._host, client_id=self._clientId, auth={'username': self._username, 'password': self._password})
            logging.info("Published %s messages", len(msgs))
        except Exception as e:
            logging.error("Error in publishing to cayenne: " + str(e))