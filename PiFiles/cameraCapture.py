import picamera
from time import sleep

print('About to take a picture.')
# setup the camera
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording('video.h264')
    sleep(5)
    camera.stop_recording()
print('Picture Taken! ')
