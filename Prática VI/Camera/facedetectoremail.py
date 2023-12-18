import cv2
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
import os
import time
from picamera2 import Picamera2

secrets = dotenv_values("Camera/.env")

from_email_addr = secrets["SENDEREMAIL"]
from_email_password = secrets["SENDERPASSWORD"]
to_email_addr = secrets["RECEIVEREMAIL"]
email_subject = "ROSTO DETECTADO"
email_body = "A câmera detectou um rosto!"

def send_email(i):
    msg = EmailMessage()
    msg.set_content(email_body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = email_subject
    msg.add_attachment(i, maintype='image', subtype='png')
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(from_email_addr, from_email_password)
    server.send_message(msg)
    server.quit()
    print('Email Sent')
    time.sleep(0.1)
    

face_detector = cv2.CascadeClassifier('/home/sel/6219/Prática VI/Camera/haarcascade_frontalface_default.xml')

cv2.startWindowThread()

picam2 = Picamera2()

picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
                 
picam2.start()

output_directory = '/home/sel/6219/Prática VI/Camera/detected_faces'

os.makedirs(output_directory, exist_ok = True)

while True:
    img = picam2.capture_array()
    
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(grey, 1.1, 5)
    
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))
        
        timestamp = int(time.time())
        filename = os.path.join(output_directory, f"face_{timestamp}.jpg")
        
        cv2.imwrite(filename, img[y:y+h, x:x+w])
        
        image = open(filename, 'rb').read()
        send_email(image)
        
    cv2.imshow("Camera", img)
    
    cv2.waitKey(1)
                    
