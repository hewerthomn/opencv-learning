import cv2 as cv
import numpy as np

def showWebcam(mirror=False):
    cam = cv.VideoCapture(0)

    if cam.isOpened():
        print("Connected to webcam...")

        while True:
            ret_val, frame = cam.read()

            if ret_val:

                if mirror:
                    frame = cv.flip(frame, 1)
                
                cv.imshow('My Webcam', frame)

                if cv.waitKey(1) == 27:
                    break # Esc to quit
        cam.release()
        cv.destroyAllWindows()

    else:
        print("Not connected to webcam")

def main():
    showWebcam(mirror=False)

if __name__ == '__main__':
    main()
