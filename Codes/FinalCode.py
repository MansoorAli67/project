# importing important libraries
from gpiozero import MotionSensor
import picamera
from datetime import datetime
from time import sleep

# setting sensor to recive output over GPIO port 4 
pir = MotionSensor(4)



# setup the loop
while True:
    # giving file path and setting rules to name a file with current time and also with format given in line 17
    filepath = "/home/pi/Desktop/Codes/SmartCam"
    currentTime = datetime.now()
    time = currentTime.strftime("%Y.%m.%d-%H%M%S")
    name = time + '.h264'
    CompletePath = filepath + name
    print('Waiting for motion.')    
    # setting camera object
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        pir.wait_for_motion
        #if else to wait for motion, where sleep is the time it need to take in order to stop recording
        if pir.motion_detected:
            camera.start_recording(name)
            pir.wait_for_no_motion
            sleep(5)
            camera.stop_recording()
            print('recording ..... Done') 
# this will print message if no motion occur and program wait for motion to occur
        print('No motion at the moment')    
