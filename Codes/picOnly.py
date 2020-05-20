import picamera

print('about to take picture')
with picamera.PiCamera() as camera:
    camera.capture("/home/pi/Desktop/Codes/SmartCam/newPic.jpg")

print('picture taken')