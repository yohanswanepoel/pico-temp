import network
import time
from secrets import *
import json
import uasyncio as asyncio
import socket

    

def do_connect(ssid=secrets['ssid'],psk=secrets['password']):
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)
    network.hostname('dd_temp')
    print(f'network hostname: {network.hostname()}')

 
    # Wait for connect or fail
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)
 
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        ip=wlan.ifconfig()[0]
        print('network config: ', ip)
        return ip
