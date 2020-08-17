import cv2 as cv
import numpy as np

def detectFace():
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    cam = cv.VideoCapture(0)
    if cam.isOpened():
        while True:
            _, frame = cam.read()

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # cv.imshow('roi gray', roi_gray)

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            frame = cv.flip(frame, 1)
            cv.imshow('My Face Detection', frame)

            if cv.waitKey(1) == 27:
                break # Esc to quit
    else:
        print('Not connected to webcam...')

def main():
    detectFace()

if __name__ == '__main__':
    main()
