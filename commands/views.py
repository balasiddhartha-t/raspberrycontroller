from django.http import HttpResponse
import RPi.GPIO as GPIO
import cv2
import os
from minio import Minio
from datetime import datetime
import ssl
import asyncio
from asgiref.sync import async_to_sync
from dotenv import load_dotenv
import pathlib

load_dotenv()


videolocation =os.environ.get('VIDEO_PATH') + os.environ.get('VIDEO_FILENAME') 
video = cv2.VideoCapture(0)
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
fps = int(video.get(cv2.CAP_PROP_FPS))
output = cv2.VideoWriter(videolocation, 
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         fps, size)


client = Minio(
    os.environ.get('MINIO_CLIENT_IP'),
    access_key=os.environ.get('MINIO_ACCESS_KEY'),
    secret_key=os.environ.get('MINIO_SECRET_KEY'),
    secure=False,
    region=os.environ.get('MINIO_REGION')
)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

def index(request):
    return HttpResponse("Hello, world. You're at the commands index. Please choose from forward/backward/right/left/stop")

async def recordVideo():
    print("wait here")


def record(request):
    print('Starting recording')
    print(videolocation)
    while (video.isOpened()):
        print("recording video here")
        ret, frame = video.read()
        if not ret:
            output.release()
        output.write(frame)
    return HttpResponse("Started Recording")

def stoprecord(request):
    video.release()
    output.release()
    found = client.bucket_exists("raspi-bucket")
    print('Starting Upload')
    if not found:
        return HttpResponse("Issue with uploading. Bucket not found")
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    print(videolocation)
    client.fput_object(
        "raspi-bucket", "record" + current_time+".mp4", videolocation,
    )
    print('Finished Uploading')
    return HttpResponse("Stopped recording")

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