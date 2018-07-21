#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from time import gmtime, strftime
import os
# from constants import _const

username = "doorbellding@gmail.com"
password = "doorbell2"
mailto = "timsdoorbell@tieka.nl"
mostrecentsnapshot = '/home/pi/Pictures/doorbellcamera/mostrecent.jpg'


def sendmail():
    print('Starting sendmail\n')
    msg = MIMEMultipart()
    text = "Hi, \n\nSomeone knocked on your door at " + strftime("%l:%M %p on %d-%m-%Y") + ".\n\nHave a great day!"
    msg['to'] = mailto
    msg['from'] = "doorbellding@gmail.com"
    msg['subject'] = "Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")

    msg.attach(MIMEText(text))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(mostrecentsnapshot, "rb").read())
    encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="photo.jpg"')

    msg.attach(part)
    print('Het bericht is:' + str(msg.as_string))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(username, password)
    server.sendmail(username, mailto, msg.as_string())
    print('\nVerzonden')
    server.quit()

