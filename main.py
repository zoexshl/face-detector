import cv2
import numpy as np

def detect_faces(frame, cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=4)
    return faces

def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.putText(frame, "Je te vois !", (x, y - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (255, 0, 0), 2)


def main():
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    while True:
        _, frame = cam.read()
        faces = detect_faces(frame, cascade)
        draw_faces(frame, faces)

        cv2.putText(frame, "Appuie sur Q pour quitter", (10, frame.shape[0] - 10), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)


        cv2.imshow("Detection de visages", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
