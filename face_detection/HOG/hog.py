import cv2
import dlib
from skimage import io
import matplotlib.pyplot as plt
import numpy as np 

frame = cv2.imread(r"C:\Users\sagar\Videos\proj\img\test1.jpg")
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face_detect = dlib.get_frontal_face_detector()
rects = face_detect(gray, 1)
for (i, rect) in enumerate(rects):
      (x, y, w, h) = face_utils.rect_to_bb(rect)
      cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

plt.imshow(frame)
plt.show()