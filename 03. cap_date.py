import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3,1500)
cap.set(4,720)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        waktu = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,waktu,(0,50),font,1,(255,255,255),2,cv2.LINE_AA)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
