import cv2
import os
from PIL import Image
import numpy as np
import pickle

def train_faces():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR,'images')
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    trained_faces = []
    labels = []
    for root, dirs, files in os.walk(image_dir):
        print(root,dirs,files)
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'):
                img_path = os.path.join(root, file)
                label = os.path.basename(root)

                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]           

                pil_image = Image.open(img_path).convert("L")
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, 'uint8')
                
                faces = face_cascade.detectMultiScale(image_array,scaleFactor=1.2,minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    trained_faces.append(roi)
                    labels.append(id_)

    with open(os.path.join(os.path.join(os.path.join(BASE_DIR, 'assests'),'serializer'),'label.pickle'), 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(trained_faces, np.array(labels))
    recognizer.save(os.path.join(os.path.join(os.path.join(BASE_DIR, 'assests'),'trainner'),'trainner.yml'))

if(__name__ == '__main__'):
    train_faces()