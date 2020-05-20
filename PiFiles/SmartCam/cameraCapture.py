from gpiozero import MotionSensor
import picamera
from time import sleep

pir = MotionSensor(4)
print('Waiting for motion.')
# setup the camera
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    pir.wait_for_motion()
    camera.start_recording('/home/pi/Desktop/Codes/SmartCam/motionVideo.h264')
    pir.wait_for_no_motion
    sleep(5)
    camera.stop_recording()
print('MotionCaptured ')