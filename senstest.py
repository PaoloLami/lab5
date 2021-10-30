import PCF8591 as ADC

sens = ADC(0x48)

def loop():
	while True:
		print (sens.read(0))
		sens.write(sens.read(0))

def destroy():
	sens.write(0)

try:
	loop()
except KeyboardInterrupt:
	destroy()