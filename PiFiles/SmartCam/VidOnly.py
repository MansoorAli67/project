import picamera
from time import sleep

with picamera.PiCamera() as camera:
   camera.start_recording("/home/pi/mu_code/SmartCam/newVid.h264")
   sleep(10)
   camera.stop_recording()
print('recording done')
