from picamera import PiCamera
from time import sleep
import random
import cv2
import numpy as np


def posterization(n, img):
    indices = np.arange(0,256)   # List of all colors 
    divider = np.linspace(0,255,n+1)[1] # we get a divider
    quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
    color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
    palette = quantiz[color_levels] # Creating the palette

    img = palette[img]  # Applying palette on image
    return cv2.convertScaleAbs(img) # Converting image back to uint8


def face_selection(img):
    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
     
    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     
    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    if len(faces) < 1:
        print "Found "+str(len(faces))+" face(s)"
        return []
    print "Found "+str(len(faces))+" face(s)"
    x, y, w, h = random.choice(faces)
    y = y-60
    if y<0:
        y=1
    x = x-60
    if x < 0:
        x=1
    return img[y:y+h+100, x:x+w+100]


def show_portrait(img):
    cv2.namedWindow("portrait", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("portrait", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow("portrait", img)
    key = cv2.waitKey(1000)
    #if key==27:
    #    cv2.destroyAllWindows()
    #    for i in range(1,5):
    #        cv2.waitKey(1)


def capture():
    camera.capture('/home/pi/test.jpg')


def destroyWindow():
    cv2.destroyAllWindows()
    for i in range(1,5):
        cv2.waitKey(1)


camera = PiCamera()
for i in range(0, 10):
    sleep(1)
    capture()
    sleep(1)
    #Load an image from file
    image = cv2.imread("/home/pi/test.jpg", 1)
    crop_image = face_selection(image)
    if len(crop_image) == 0:
        continue
    p_level = [2, 4, 8]
    crop_image = posterization(random.choice(p_level), crop_image) 
    show_portrait(crop_image)


destroyWindow()