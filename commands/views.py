import RPi.GPIO as GPIO
import os
import time
from dotenv import load_dotenv
from django.http import HttpResponse
from django.shortcuts import render


load_dotenv()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def index(request):
    return render(request, 'index.html')

#Execute a bunch of commands to start and stop the raspi
def command(request, command):
    if command == "forward":
        print("Command Backward  has been called")
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)

    elif command == "backward":
        print("Command Forward has been called")
        GPIO.output(3, False)
        GPIO.output(5, True)
        GPIO.output(8, False)
        GPIO.output(10, True)


    elif command == "left":
        print("Command Left has been called")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)
        time.sleep(2)
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)

    elif command == "right":
        print("Command Right has been called")
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, False)
        GPIO.output(10, False)
        time.sleep(2)
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)

    elif command == "stop":
        print("Command Stop has been called")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(8, False)
        GPIO.output(10, False)
    else:
        print(command)
        return HttpResponse("This Command doesn't exist. Please choose from forward/backward/right/left/stop")
    print("Your " + command +" Command has been executed")
    return render(request, 'index.html')