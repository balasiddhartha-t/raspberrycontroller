from django.shortcuts import render
from raspberrysite.commons import record

# Request to record the video
def startrecord(request):
    record.start()
    return render(request, 'index.html')

# Request to stop recording the video
def stoprecord(request):
    record.stop()
    return render(request, 'index.html')