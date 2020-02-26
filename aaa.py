import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)
print('cap')
while(True):
    # Capture frame-by-frame
    
    ret = False
    while(ret == False):
        ret, frame = cap.read()

   

    print('ret:')
    print(ret)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    print('cv2.imshow')
    cv2.imshow('frame',frame)
    print('after cv2.imshow')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()