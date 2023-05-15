import network
import socket
from time import sleep
import machine
from umqtt.simple import MQTTClient
import random

import wificonnect
print("Connected to Wifi.")

mqtt_server = 'io.adafruit.com'
mqtt_port = 1883 # non-SSL port
mqtt_user = 'YOUR_ADAFRUIT_ID_HERE' #Adafruit ID
mqtt_password = 'YOUR_ADAFRUIT_KEY_HERE' # Under Keys
mqtt_topic = 'YOUR_ADAFRUIT_ID_HERE/feeds/YOUR_FEED_NAME_HERE' # Under "Feed info"
mqtt_client_id = str(random.randint(10000,999999)) #must have a unique ID - good enough for now


def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, server=mqtt_server, port=mqtt_port, user=mqtt_user, password=mqtt_password, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
    
while True:
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        client.publish(mqtt_topic, '10')
    else:
        reconnect()
    sleep(20)
