import cv2

def detectFace():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        while True:
            _, frame = cam.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # cv2.imshow('roi gray', roi_gray)

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            frame = cv2.flip(frame, 1)
            cv2.imshow('My Face Detection', frame)

            if cv2.waitKey(1) == 27:
                break # Esc to quit
    else:
        print('Not connected to webcam...')

def main():
    detectFace()

if __name__ == '__main__':
    main()
