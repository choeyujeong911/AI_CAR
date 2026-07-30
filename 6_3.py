import mycamera
import cv2
import time
from pathlib import Path

def main():
    camera = mycamera.MyPiCamera(640,480)
  
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        
        if keyValue == ord('q'):
            break
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        cv2.imwrite(f"{Path.home()}/AI_CAR/video/test.png" , image)
        
        time.sleep(1.0)
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
