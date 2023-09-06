import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitkey(10) == ord('q'):
        break
    cv2.imshow('seccam', frame)
