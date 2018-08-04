from picamera import PiCamera
camera = PiCamera()

for i in range(10000):
    if(i==10000):
        i=0        
    camera.capture('timelapse/image{0:04d}.jpg'.format(i))
    wait(10)
