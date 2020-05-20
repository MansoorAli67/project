from gpiozero import MotionSensor
import picamera
from datetime import datetime
from time import sleep

pir = MotionSensor(4)
print('Waiting for motion.')
filepath = "/home/pi/Desktop/Codes/SmartCam"
currentTime = datetime.now()
time = currentTime.strftime("%Y.%m.%d-%H%M%S")
name = time + '.h264'
CompletePath = filepath + name

# setup the camera
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    pir.wait_for_motion
    camera.start_recording(name)
    pir.wait_for_no_motion
    sleep(5)
    camera.stop_recording()
print('recording done')    
    