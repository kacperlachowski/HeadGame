import cv2


def face_reader(var_global):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)

    img_counter = 0

    last_x = -1

    while True:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        k = cv2.waitKey(1)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if last_x + 10 < x or last_x - 10 > x:
                last_x = x
                var_global.insert(0, x)

        # Display the resulting frame
        cv2.imshow('FaceDetection', frame)

        if k % 256 == 32:  # SPACE pressed
            img_name = "facedetect_webcam_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    video_capture.release()
    cv2.destroyAllWindows()
