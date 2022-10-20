from pkgutil import read_code
import face_recognition as fr
import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import cv2
from face_detection import *


def recognize_faces(img):
    target = dict()
    a = 0
    for p in os.listdir(r'.\dataset'):
        target[p] = a
        a += 1
    reverse_target = dict([(v,k) for k,v in target.items()])

    try:
        f = open("./facenet_knn.pickle", 'rb')
        model = pickle.load(f)
        f.close()
    except:
        print("Something went wrong!")
        os._exit(1)
    # img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    img = np.uint8(img)
    cropped_faces, img = face_detection_2(img)
    # print(len(cropped_faces), cropped_faces[0].shape)
    # plt.imshow(img)
    # plt.show()

    ans = dict()
    face_vs_name = []
    for i,face in enumerate(cropped_faces):
        # plt.imshow(face)
        # plt.show()
        unknown_encoding = fr.face_encodings(face ,num_jitters=3 , model='large')
        if len(unknown_encoding):
            ans = model.predict(unknown_encoding)
            face_vs_name.append(reverse_target[ans[0]])
        else :
            face_vs_name.append("~ENCODING")

    # fig, axes = plt.subplots( math.ceil(len(face_vs_name)/2) , 2 )
    # for i,face in enumerate(cropped_faces):
    #     axes.ravel()[i].imshow(face)
    #     axes.ravel()[i].set_title(face_vs_name[i])
    #     axes.ravel()[i].axis('off')
    # fig.tight_layout()
    # plt.show()

    return face_vs_name

if __name__ == '__main__':
    vid = cv2.VideoCapture(0)

    while (True):
        ret, frame = vid.read()
  
        # Display the resulting frame
        cv2.imshow('frame', frame)
        print(recognize_faces(frame))
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break