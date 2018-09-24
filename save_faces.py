import cv2
import time

cap = cv2.VideoCapture(0)
img_no = 1

while True:
    return_value, image = cap.read()
    cv2.imwrite('opencv'+str(img_no)+'.png', image)
    img_no += 1
    if(img_no >= 10):
        break
    cv2.imshow('frame',image)
    cv2.waitKey(2000)


cap.release()
cv2.destroyAllWindows()