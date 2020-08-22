import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

# fourcc = cv.VideoWriter_fourcc(*'XVID') # Use on linux
fourcc = cv.VideoWriter_fourcc(*'MJPG') # Use on Osx
out = cv.VideoWriter('04-output.avi', fourcc, 20.0, size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cant't receive frame (stream end?). Exiting...")
        break
    frame = cv.flip(frame, 1)

    # write the flipped frame
    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break # Esq to quit

cap.release()
out.release()
cv.destroyAllWindows()