from subprocess import call
from datetime import datetime
from time import sleep
import picamera
import os
from send_email_attachment import sendmail
from tweet import tweet
from shutil import copyfile
# from constants import _const

#directories
globdir = "/home/pi" #homedirectory
dir_sounds = "%s/doorbell/sounds" % globdir #wav's, mp3's and amr's
dir_images = "%s/doorbell/images" % globdir #where the pi's desktop images are kept
dir_camera_images = "%s/Pictures/doorbellcamera" % globdir # photo's and video's taken by the camera


class Ringer(object):

    def __init__(self):
        try:
            print("Ringer uses these directories:")
            print(dir_sounds)
            print(dir_images)
            print(dir_camera_images)
            self.camera = picamera.PiCamera()
            self.camera.resolution = (1024, 768)
        except:
            print('Something went horribly wrong. I lost my camera and can''t start it again without rebooting. So I will now reboot within 5 seconds.')
            sleep(5)
            # os.system('sudo shutdown -r now')

    def __del__(self):
        self.camera.close()

    def respond(self):
        print("Ringer respond function triggered")
        datetimestamp = datetime.now().isoformat()
        newfile = "%s/visitor%s.jpg" % (dir_camera_images, datetimestamp)
        self.camera.capture(newfile)
        self.camera.close()
        # and copy the new image to the most recent snapshot to show on our inhouse-answering-devices
        mostrecentsnapshot = "%s/mostrecent.jpg" % dir_camera_images
        copyfile(newfile, mostrecentsnapshot)

class FamilyOrFriend(Ringer):
    def respond(self):
        
        super(FamilyOrFriend, self).respond() # Works fine
        mp3sound = "%s/he_hallo_is_daar_iemand.wav" % dir_sounds # Works fine
        os.system('aplay -D plughw:CARD=Device_1,DEV=0 %s' % mp3sound) #as alternative to omxplayer 
#         call(["omxplayer", mp3sound, "-o", "alsa"]) # Works fine
        sendmail()  # Works fine.
#        tweet()  # Works fine.
# Todo2 make this work, Ekiga.net (and Twinkle) and the phone-app of linphone
        os.system("./call.sh") # does not work. Fails to connect to the phone


class Salesman(Ringer):
    def respond(self):
        super(Salesman, self).respond()
        print("bugger off!!")
        sleep(1)


class Deliverer(Ringer):
    def respond(self):
        super(Deliverer, self).respond()
        mp3sound = "%s/sounds/beep-03.mp3" % dir_sounds
        call(["omxplayer",mp3sound, "-o", "alsa"])


class HansOrGrietje(Ringer):
    def respond(self):
        super(HansOrGrietje, self).respond()
        mp3sound = "%sdoorbell/sounds/knibbelknabbelknuisje.amr" % dir_sounds
        call(["omxplayer",mp3sound, "-o", "alsa"])