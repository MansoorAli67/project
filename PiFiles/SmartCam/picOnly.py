import picamera

print('about to take picture')
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/mu_code/SmartCam/newPic.jpg")

print('picture taken')