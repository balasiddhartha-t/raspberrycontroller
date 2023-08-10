from django.shortcuts import render
from raspberrysite.commons import record

from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.shortcuts import render


#Request to view the live feed
def video_feed(request):
    print("Inside here")
    return StreamingHttpResponse(record.generate_frames(), content_type='multipart/x-mixed-replace;boundary=frame')

def viewfeed(request):
    return render(request, 'record.html')


import cv2
from django.http import HttpResponse
from django.views.decorators import gzip
import threading
# Lock for thread safety
global_frame = None
frame_lock = threading.Lock()



from django.shortcuts import render

def video_stream_page(request):
    return render(request, 'record.html')



def video_stream(request):
    return StreamingHttpResponse(record.generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


# Request to record the video
def startrecord(request):
    record.start()
    return render(request, 'index.html')

# Request to stop recording the video
def stoprecord(request):
    record.stop()
    return render(request, 'index.html')

