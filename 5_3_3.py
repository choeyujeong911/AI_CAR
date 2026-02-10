import cv2
import numpy as np

pl = (
    "libcamerasrc ! video/x-raw,format=NV12,width=160,height=120,framerate=20/1 !"
    "videoconvert ! video/x-raw,format=BGR ! appsink drop=1 sync=false"
)

def main():
    camera = cv2.VideoCapture(pl)
    camera.set(3, 160)
    camera.set(4, 120)
    
    while(camera.isOpened()):
        ret, frame = camera.read()
        frame = cv2.flip(frame, -1)
        cv2.imshow('normal', frame)

        crop_img = frame[60:120, 0:160]
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)

        cv2.imshow('crop+gray+blur', blur)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()