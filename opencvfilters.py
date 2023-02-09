#simple video filter program
import cv2
  
filter = input("Enter filter (c)Color, (g)Grayscale (i)Invert: ")

vid = cv2.VideoCapture(0)
  
while(True):
    ret, frame = vid.read()
    if filter == "g":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if filter == "i":
        frame = cv2.bitwise_not(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()