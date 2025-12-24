import cv2

pl = (
    "libcamerasrc ! video/x-raw,format=NV12,width=640,height=480,framerate=20/1 !"
    "videoconvert ! video/x-raw,format=BGR ! appsink drop=1 sync=false"
)

def main():
    camera = cv2.VideoCapture(pl)
    camera.set(3, 640)
    camera.set(4, 480)
    print(camera.isOpened())
    
    while(camera.isOpened()):
        _, image = camera.read()
        cv2.imshow('camera test', image)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()