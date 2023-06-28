from django.http import HttpResponse
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def index(request):
    return HttpResponse("Hello, world. You're at the commands index. Please choose from forward/backward/right/left/stop")


def command(request, command):
    if command == "backward":
        print("Command Forward has been called")
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)
    elif command == "forward":
        print("Command Backward has been called")
        GPIO.output(3, False)
        GPIO.output(5, True)
        GPIO.output(8, False)
        GPIO.output(10, True)
    elif command == "right":
        print("Command Right has been called")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(8, True)
        GPIO.output(10, False)
    elif command == "left":
        print("Command Left has been called")
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(8, False)
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
    return HttpResponse("Your " + command +" Command has been executed")