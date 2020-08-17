import cv2

def showWebcam(cv2, mirror=False):
    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        print("Connected to webcam...")

        while True:
            ret_val, frame = cam.read()

            if ret_val:

                if mirror:
                    frame = cv2.flip(frame, 1)
                
                cv2.imshow('My Webcam', frame)

                if cv2.waitKey(1) == 27:
                    break # Esc to quit
        cv2.destroyAllWindows()
    else:
        print("Not connected to webcam")

def main():
    showWebcam(cv2, mirror=True)

if __name__ == '__main__':
    main()
