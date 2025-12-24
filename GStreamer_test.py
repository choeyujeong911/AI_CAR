import cv2

info = cv2.getBuildInformation()
for l in info.splitlines():
    if "GStreamer" in l or "Video I/O" in l:
        print(l)