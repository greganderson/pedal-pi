import RPi.GPIO as GPIO
from time import sleep
from socket import *


GPIO.setmode(GPIO.BCM)

button = 17
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = 1
current_state = 0

next_page = 'Next page :)'.encode('UTF-8')
previous_page = 'Previous page :)'.encode('UTF-8')

ip_address = '192.168.1.255'
port = 9050

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# TODO: Add previous page button
try:
	print('Getting ready to turn some pages!')
	while True:
		current_state = GPIO.input(button)
		if last_state == GPIO.LOW and current_state == GPIO.HIGH:
			print('Sending a message to turn the page...')
			cs.sendto(next_page, (ip_address, port))
			#cs.sendto(previous_page, (ip_address, port))
			sleep(1)
		last_state = current_state
except KeyboardInterrupt:
	print('Ending my joyous journey of page turning.')
	exit(0)
