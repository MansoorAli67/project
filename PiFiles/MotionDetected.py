from gpiozero import MotionSensor
import picamera
from time import sleep

pir = MotionSensor(4)
print('Waiting for motion')

# setup the camera
with picamera.PiCamera() as camera:
    pir.wait_for_motion()
    camera.start_recording('intruder.h264')
    pir.wait_for_no_motion()
    camera.stop_recording()
print("Motion Detected")