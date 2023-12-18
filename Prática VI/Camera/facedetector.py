import cv2
import os
import time
from picamera2 import Picamera2

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
        
    cv2.imshow("Camera", img)
    
    cv2.waitKey(1)
                    