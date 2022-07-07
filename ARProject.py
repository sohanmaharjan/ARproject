import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (w-10, h-10))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
    cv2.imshow('Augmented Reality', frame)
    if cv2.waitKey(10) == ord('q'):
        break