import RPi.GPIO as GPIO
import signal
import sys
import os
from dotenv import load_dotenv

load_dotenv()

motor1_f = int(os.getenv('RASPI_FORWARD_MOTOR1', 3))
motor1_b = int(os.getenv('RASPI_FORWARD_MOTOR2', 5))
motor2_f = int(os.getenv('RASPI_BACKWARD_MOTOR1', 8))
motor2_b = int(os.getenv('RASPI_BACKWARD_MOTOR2', 10))



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1_f, GPIO.OUT)
GPIO.setup(motor1_b, GPIO.OUT)
GPIO.setup(motor2_f, GPIO.OUT)
GPIO.setup(motor2_b, GPIO.OUT)



def forward():
    GPIO.output(motor1_f, True)
    GPIO.output(motor1_b, False)
    GPIO.output(motor2_f, True)
    GPIO.output(motor2_b, False)

def backward():
    GPIO.output(motor1_f, False)
    GPIO.output(motor1_b, True)
    GPIO.output(motor2_f, False)
    GPIO.output(motor2_b, True)


def left():
    GPIO.output(motor1_f, False)
    GPIO.output(motor1_b, False)
    GPIO.output(motor2_f, True)
    GPIO.output(motor2_b, False)

def right():
    GPIO.output(motor1_f, True)
    GPIO.output(motor1_b, False)
    GPIO.output(motor2_f, False)
    GPIO.output(motor2_b, False)

def stop():
    GPIO.output(motor1_f, False)
    GPIO.output(motor1_b, False)
    GPIO.output(motor2_f, False)
    GPIO.output(motor2_b, False)



def clear(*args):
    GPIO.cleanup()
    sys.exit(0) 
    
signal.signal(signal.SIGINT, clear)
