import network
import socket
from time import sleep
import machine

ssid = 'WIFI SSID HERE'
password = 'WIFI PASSWORD HERE'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection... ')
        if wlan.status() == network.STAT_NO_AP_FOUND:
            print("No access point found with the ssid " + ssid)
            break
        if wlan.status() == network.STAT_WRONG_PASSWORD:
            print("Password rejected by WLAN.")
            break
        if wlan.status() == network.STAT_CONNECT_FAIL:
            print("Connection failed.")
            break
        sleep(1)
    print(wlan.ifconfig())

try:
    connect()
except KeyboardInterrupt:
    machine.reset()
