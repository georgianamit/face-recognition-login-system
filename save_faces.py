import cv2
import time
import os

def save_detected_faces(username):
    cap = cv2.VideoCapture(0)
    img_no = 1
    count = 50
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.join(os.path.join(BASE_DIR, 'assests'),'images'),username)
    try:
        os.mkdir(path)
    except:
        pass
    image_dir = path

    while count > 0:
        count -= 1
        return_value, image = cap.read()

        if(count%5 == 0):
            cv2.imwrite(os.path.join(image_dir, str(img_no)+'.png'), image)    
            img_no += 1
        cv2.imshow('frame',image)
        cv2.waitKey(200)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    save_detected_faces('spider')