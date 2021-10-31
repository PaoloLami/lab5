import RPi.GPIO as GPIO
import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))
        

pins = [18,21,22,23] #controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.OUT, initial=0)

#Define the pin sequence for counter-clockwise motion, noting that
#two adjacent phases must be actuated together before stepping to
#a new phase so that the rotor is pulled in the right direction:

sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 #current position in stator sequence

def delay_us(tus): #use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir): #DOESNT STOP
  #dir  = +/-1 (ccw/cw)
  global state, pins, sequence
  state += 1 #FIX THIS DIR
  if state > 7: state = 0
  elif state < 0: state = 7
  for pin in range(4): #4 pins that need to be energized
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[pin], GPIO.OUT, initial=0)
    GPIO.output(pins[pin],sequence[state][pin])
  delay_us(1000) #decrease to make stepper motor faster
  GPIO.cleanup()
  
def moveSteps(steps,dir):
  #move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)

def goAngle(ang,dir):
  numhalfstep = int(ang/0.3515)
  for step in range(numhalfstep):
      halfstep(dir)
      
sens = PCF8591(0x48)

def zero(): #WOORKING, check sensitivity everytime
  
  ledPin = 19
  light = sens.read(0)*10
  print(light)
  
  while light > 455:
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, 1)  
    light = sens.read(0)*10  
    print(light)
    halfstep(1)
    
  if light < 450:
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(ledPin, GPIO.OUT) 
      GPIO.output(ledPin,0) 