import cv2
import os
import threading
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

# Minio Client Initialize
client = Minio(
    os.environ.get('MINIO_CLIENT_IP'),
    access_key=os.environ.get('MINIO_ACCESS_KEY'),
    secret_key=os.environ.get('MINIO_SECRET_KEY'),
    secure=False,
    region=os.environ.get('MINIO_REGION')
)

# Get the indices for the video that is currently available
def get_video_indices():
    devs = os.listdir('/dev')
    vid_indices = [int(dev[-1]) for dev in devs 
            if dev.startswith('video')]
    vid_indices = sorted(vid_indices)
    return vid_indices

# Set the parameters for Video
vid_indices = get_video_indices()
videoname = os.environ.get('VIDEO_FILENAME') +".mp4"
videolocation = os.environ.get('VIDEO_PATH') + os.environ.get('VIDEO_FILENAME')
video = cv2.VideoCapture(vid_indices[0])
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
fps = int(video.get(cv2.CAP_PROP_FPS))
output = cv2.VideoWriter(videolocation, 
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         fps, size,)


# Record the video in a separate thread in background
def background_record(request, videolocation=videolocation):
    vid_indices = get_video_indices()
    global video
    camera_idx = vid_indices[0]
    print("camera_idx ============================")
    print(camera_idx)
    video = cv2.VideoCapture(camera_idx)
    print("videolocation ============================")
    print(videolocation)
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    output = cv2.VideoWriter(videolocation, 
                         cv2.VideoWriter_fourcc(*'mp4v'),
                        fps, size)

    while (video.isOpened()):
        print("recording video here "+ videolocation )
        ret, frame = video.read()
        if not ret:
            output.release()
        output.write(frame)
    


# Request to record the video
def record(request):
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    global videoname
    videoname = os.environ.get('VIDEO_FILENAME')  + current_time+".mp4"
    global videolocation
    videolocation = os.environ.get('VIDEO_PATH') + videoname
    thread = threading.Thread(target=background_record(request = request, videolocation=videolocation))
    thread.start()
    return render(request, 'index.html')

# Request to stop recording the video
def stoprecord(request):
    global video
    output.release()
    video.release()
    found = client.bucket_exists(os.environ.get('MINIO_BUCKET_NAME'))
    print('Starting Upload')
    if not found:
        return HttpResponse("Issue with uploading. Bucket not found")

    global videolocation
    global videoname
    print(videoname)
    client.fput_object(
        os.environ.get('MINIO_BUCKET_NAME'), videoname, videolocation,
    )
    os.remove(videolocation)
    print("Stopped recording uploaded video with name " + videoname +" to location "+ videolocation)
    return render(request, 'index.html')