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

wlan = network.WLAN(network.STA_IF)

def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, server=mqtt_server, port=mqtt_port, user=mqtt_user, password=mqtt_password, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    sleep(5)
    machine.reset()

def process_message(topic, msg):
    print("Received a message:" + str(msg))
    # Put any other message handling logic here.

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()

client.set_callback(process_message)
client.subscribe(mqtt_topic)
    
while True:
    if wlan.isconnected():
        try:
            client.wait_msg() # This is a blocking function, which means no other code will be executed while waiting for a message.
        except OSError as e:
            reconnect()
    else:
        reconnect()
