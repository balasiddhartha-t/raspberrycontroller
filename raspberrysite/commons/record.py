import datetime
import cv2
import os
import threading
from datetime import datetime
from django.shortcuts import render
from dotenv import load_dotenv
from raspberrysite.commons import storage


load_dotenv()


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
output = cv2.VideoWriter(videolocation, cv2.VideoWriter_fourcc(*'MP4V'), fps, size, False)

customstop = True

def start():
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    global videoname
    videoname = os.environ.get('VIDEO_FILENAME')  + current_time+".mp4"
    global videolocation
    videolocation = os.environ.get('VIDEO_PATH') + videoname
    thread = threading.Thread(target=background(videolocation=videolocation))
    thread.start()
    return "Started recording..."




# Record the video in a separate thread in background
def background(videolocation=videolocation):
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
    output = cv2.VideoWriter(videolocation, cv2.VideoWriter_fourcc(*'MP4V'), fps, size, False)
    while (video.isOpened()):
        ret, frame = video.read()
        if not ret:
            output.release()
        output.write(frame)


# Request to stop recording the video
def stop():
    global output
    output.release()
    global video
    video.release()
    found = storage.getBucket(os.environ.get('MINIO_BUCKET_NAME'))
    
    if not found:
        return "Issue with uploading. Bucket not found"

    global videolocation
    print(videolocation)
    global videoname
    print(videoname)
    
    if (os.path.isfile(videolocation)) :
        print('Starting Upload')
        storage.putObject( os.environ.get('MINIO_BUCKET_NAME'), videoname, videolocation)
        os.remove(videolocation)
        videoname = os.environ.get('VIDEO_FILENAME') +".mp4"
        customstop = True
    else:
        return "error occurred while uploading/deleting the video"
    
    return "Stopped recording... Uploaded video with name " + videoname +" to location "+ videolocation
    