import cv2 as cv
import numpy as np

WEBCAM_INDEX = 0

def detectFace():
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    cam = cv.VideoCapture(WEBCAM_INDEX)

    if not cam.isOpened():
        print('Webcam not connected')
    else:
        while True:
            ret, frame = cam.read()
            if ret:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x,y,w,h) in faces:
                    cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]

                    # cv.imshow('roi colorr', roi_color)
                    cv.imwrite('last-detected-face.jpg', frame)

                frame = cv.flip(frame, 1)
                cv.imshow('My face detection', frame)

                if cv.waitKey(1) == 27: # Esc to quit
                    break
        cam.release()
        cv.destroyAllWindows()

def main():
    detectFace()

if __name__ == '__main__':
    main()
