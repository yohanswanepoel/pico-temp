import network
import time
import sys
import json
from PiicoDev_TMP117 import PiicoDev_TMP117

from microdot import Microdot

from utils import *

do_connect()
print("Connected to Wifi 2")

app = Microdot()
tempSensor = PiicoDev_TMP117()


@app.route('/')
async def get_temp(request):
  temp_c = tempSensor.readTempC()
  result = {
    'temperature': temp_c,
    'metric': 'Celcius'
  }
  return json.dumps(result)

app.run(port=6000)