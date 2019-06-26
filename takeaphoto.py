import RPi.GPIO as GPIO 

from time import sleep 
from picamera import PiCamera

camera = PiCamera()

camera.annotate_text = "Smile! Rasberry Pi will now take your picture!"

print(GPIO.RPI_INFO)

#setmode identifies what layout style of pins we're using, the one related directly
#to the board is called GPIO.BOARD vs GPIO.BCM 
GPIO.setmode(GPIO.BOARD)

#setting up an output pin 
pin11 = 11

GPIO.setup(pin11, GPIO.OUT, initial = 0)

#Now states can either be GPIO.HIGH or true or 1 or GPIO.LOW or false or 0

#Let's blink the LED

#Changing the state requires 

#while True:
	#Changing the state requires 
#	GPIO.output(pin11, 1)

#	sleep(2)

#	GPIO.output(pin11, GPIO.LOW)

#	sleep(2)

pin13 = 13

GPIO.setup(pin13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x = None 

while (True): 
	if GPIO.input(pin13) == GPIO.HIGH:
		print("BUTTON PRESSED")
		GPIO.output(pin11, GPIO.HIGH) 
		camera.start_preview()
		sleep(5)
		camera.capture('/home/pi/Desktop/RASPIPIC.jpg')
		GPIO.output(pin11, GPIO.LOW)
		camera.stop_preview()
		exit()


