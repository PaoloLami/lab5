import RPi.GPIO as GPIO
import time
import PCF8591 as ADC

GPIO.setmode(GPIO.BCM)

ledPin = 19
GPIO.setup(ledPin, GPIO.OUT)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 # current position in stator sequence

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir  = +/-1 (ccw/cw)
  state += dir
  if state > 7: state = 0
  elif state < 0: state = 7
  for pin in range(4): # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000) #decrease to make stepper motor faster

def moveSteps(steps,dir):
  # move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)

def goAngle(ang,dir):
  numhalfstep = int(ang/0.3515)
  for step in numhalfstep:
      halfstep(dir)

def zero():
  sens = ADC(0x48)
  light = sens.write(sens.read(0))
  while light < 50:
    GPIO.output(ledPin, 1)
    halfstep(1)
  GPIO.output(ledPin, 0)

try:
  moveSteps(1000,1) #move 1000 steps in ccw direction
except:
  pass
GPIO.cleanup()