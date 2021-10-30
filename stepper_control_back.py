import RPi.GPIO as GPIO
import stepper
import time
from urllib.request import urlopen  # use to send/receive data
from urllib.parse import urlencode  # use to structure a GET string

anglePREV = 0
ledPin = #

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
api = "GA4XGELVZMZ7IXTQ"

try:
  while True:
    with open('angle.txt', 'w') as f:
      angleNEW = f.readlines()[-1]
      anglePREV = f.readlines()[-2]
      angle = angleNEW - anglePREV
      if angle > 0
        dir = -1
      elif angle < 0
        dir = 1
      stepper.goAngle(angle,dir)

      #Send results to Thingspeak
      params = {
        1: angleNEW,
        "api_key":api}
      params = urlencode(params)   # reformat dictionary as a GET string
      url = "https://api.thingspeak.com/update?" + params
      response = urlopen(url)      # open the URL 
      print(response.status, response.reason) # display request response
      time.sleep(15.1)    # 15 sec minimum

except KeyboardInterrupt:
  print("Exiting...")
    
    