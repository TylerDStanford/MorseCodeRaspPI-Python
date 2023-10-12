import RPi.GPIO as GPIO
from time import sleep 
from pyMorseTranslator import translator 
#I imported a libarary that is a morse code translator and also the GPIO libarary
#This way I can trasnlate the input and write a basic for
#loop to display the morse message audibly. I also imported time so we can use
#the sleep function
buzzer = 13
encoder = translator.Encoder()
decoder = translator.Decoder()
touchPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(touchPin,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(buzzer,10)
# For this first part we just set a bunch of values. We instantiate the pin 
# of our buzzer and touch sensor by creating two variables and setting thier
#values to what pin we want them to be. We also define our encoder and decoder
# this is just so itll be easier to use the morse code library and encode our
#message. We also setup both of the pins we will be using by making our
#touchpin set to input and our buzzer pin set to output. We also set warnings
#to false which just makes our program cleaner when we run it aswell as setting
# our buzzer's frequency to 10 hz and holding it in the variable p. 

def on_key_press(): #This is a function for when the user wants to input a word
# or sentence and we want to convert it to morse code.
	
	x = input()
	morse_x = (encoder.encode(x).morse)
	print(morse_x) #This is getting the input from our user and convering
# it to morse code which will be stored in morse_x
	for i in morse_x: #this is the for loop that turns the morse message
# into sound.
		if i == "-":
			p.start(1) #this turns on our buzzer and emits a sound
			sleep(0.8) #This makes it so our buzzer plays sound for
# 0.8 seconds
			p.stop() #this turns off our buzzer stopping sound
			sleep(0.2)
		elif i ==".":
			p.start(1)
			sleep(0.2)
			p.stop()
			sleep(0.2)
		elif i == " ":
			sleep(0.2)

def keyboard_inpput(): # this is for when we want to turn input from our touch
# sensor into sound
	xs = True
	while xs:
		val = GPIO.input(touchPin) #this is getting the value of our
# touchpin and whehter or not it is on or off,
# or whether or not we are touching it
		if (val == 1):
			p.start(1)
		elif (val == 0):
			p.stop()		


try: # this is useful because it allows us to switch from sensor mode to input
# mode by the user pressing ctrl+c

	keyboard_inpput()

except KeyboardInterrupt:
	on_key_press()
