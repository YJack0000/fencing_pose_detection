import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1920,1080))

faceCascade = cv2.CascadeClassifier('./face_detect.xml')

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceRect = faceCascade.detectMultiScale(gray, 1.1, 10)

    for (x, y, w, h) in faceRect:
        cv2.rectangle(frame, (int(x), int(y)), (x+w, y+h), (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow('frame', frame)

    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()