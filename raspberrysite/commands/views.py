import time
from dotenv import load_dotenv
from django.http import HttpResponse
from django.shortcuts import render
from raspberrysite.commons import gpio

load_dotenv()



def index(request):
    return render(request, 'index.html')

#Execute a bunch of commands to start and stop the raspi
def command(request, command):
    if command == "forward":
        print("Command Backward  has been called")
        gpio.forward()

    elif command == "backward":
        print("Command Forward has been called")
        gpio.backward()

    elif command == "left":
        print("Command Left has been called")
        gpio.left()
        time.sleep(1)
        gpio.forward()

    elif command == "right":
        print("Command Right has been called")
        gpio.right()
        time.sleep(1)
        gpio.forward()

    elif command == "stop":
        print("Command Stop has been called")
        gpio.stop()
    else:
        print(command)
        return HttpResponse("This Command doesn't exist. Please choose from forward/backward/right/left/stop")
    print("Your " + command +" Command has been executed")
    return render(request, 'index.html')