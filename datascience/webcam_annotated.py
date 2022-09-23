import cv2

video = cv2.VideoCapture(0)

while True:
    status, frame = video.read()
    cv2.flip(frame, 1, frame)

    cv2.rectangle(frame, (0,0), (frame.shape[1],50), (255, 255 , 255), -1)

    cv2.putText(frame, 'Live', (10,40),
        cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),1,)
        
    cv2.putText(frame, 'Webcam 0', (frame.shape[1]//2-100,40),
        cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),1)

    cv2.imshow("webcam 0", frame)  
    if cv2.waitKey(1) == ord('q'):  
        break
video.release()                      
cv2.destroyAllWindows()              
