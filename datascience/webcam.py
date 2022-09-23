import cv2

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if not check:
        break
    cv2.imshow("webcam 0", frame)   #displays a window with the webcam
    if cv2.waitKey(1) == ord('q'):  # if the key is q, the loop breaks
        break
video.release()                      #release the webcam
cv2.destroyAllWindows()              #closes all windows
