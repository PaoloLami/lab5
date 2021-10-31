import RPi.GPIO as GPIO
import stepper
from urllib.request import urlopen  # use to send/receive data
from urllib.parse import urlencode  # use to structure a GET string

ledPin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT) 
anglePREV = 0
api = "GA4XGELVZMZ7IXTQ"

try:
  while True:
    with open('angle.txt', 'r') as f:
      angleNEW = int(f.read())
    angle = angleNEW - anglePREV
    print(angle)
    if angle > 0:
      dir = 1  
    if angle < 0:
      dir = -1
    if angleNEW == 0:
      GPIO.output(ledPin,1) 
      stepper.zero()
      GPIO.output(ledPin,0)    
    else:
      stepper.goAngle(angle,dir)
  
    anglePREV = angleNEW

    #Send results to Thingspeak
    params = {
      1: angleNEW,
      "api_key":api}
    params = urlencode(params)   # reformat dictionary as a GET string
    url = "https://api.thingspeak.com/update?" + params
    response = urlopen(url)      # open the URL 
    
except KeyboardInterrupt:
  print("Exiting...")
    
    
    
    