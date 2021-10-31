import RPi.GPIO as GPIO
import stepper
import time
from urllib.request import urlopen  # use to send/receive data
from urllib.parse import urlencode  # use to structure a GET string

api = "GA4XGELVZMZ7IXTQ"

try:
  while True:
    with open('angle.txt', 'r') as f:
      #angleNEW = f.readlines()[-1]
      #anglePREV = f.readlines()[-2]
      angle = int(f.read())
      print(angle)
      if angle > 0:
          stepper.goAngle(angle,1)
      elif angle == 0:
          stepper.zero()  

      #Send results to Thingspeak
      params = {
        1: angle,
        "api_key":api}
      params = urlencode(params)   # reformat dictionary as a GET string
      url = "https://api.thingspeak.com/update?" + params
      response = urlopen(url)      # open the URL 
      print(response.status, response.reason) # display request response
    

except KeyboardInterrupt:
  print("Exiting...")
    
    
    
    