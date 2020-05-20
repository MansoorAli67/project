from gpiozero import MotionSensor

pir = MotionSensor(4)
print('Waiting for motion')

pir.wait_for_motion()
print("Motion Detected")    
    
pir.wait_for_no_motion()
