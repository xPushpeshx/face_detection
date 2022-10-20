import face_recognition as fr
import os
import pickle
import sys
import cv2, dlib, math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

base =  r".\dataset"
names = os.listdir(base)                # names of people
person_face_encodings = dict()


for name in names:
    person_face_encodings[name] = []
    for file_name in os.listdir(base+'/'+name):
        img = fr.load_image_file(base+'/'+name+'/'+file_name)
        encodings = fr.face_encodings(img, model='large')
        if len(encodings):
            person_face_encodings[name].append(encodings[0])

try:
    f = open("./important files/face_encodings.pickle", 'wb')
    pickle.dump(person_face_encodings, f)
    f.close()
except:
    print("Something went wrong!")
    os._exit(1)

try:
    f = open("./important files/face_encodings.pickle", 'rb')
    person_face_encodings = pickle.load(f)
    f.close()
except:
    print("Something went wrong!")
    os._exit(1)


target = dict()

a = 0
for p in list(person_face_encodings.keys()):
    target[p] = a
    a += 1
reverse_target = dict([(v,k) for k,v in target.items()])
target

X = []
y = []

for k,v in person_face_encodings.items():
    for i in v:
        X.append(i)
        y.append(target[k])

X = np.array(X)
y = np.array(y)

knn = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
knn.fit(X,y)

try:
    f = open("./important files/facenet_knn.pickle", 'wb')
    pickle.dump(knn, f)
    f.close()
except:
    print("Something went wrong!")
    os._exit(1)
print("model saved")