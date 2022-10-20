import dlib , cv2

# This function is computationally expensive:
def face_detection_1(img):
    """Extract the faces from the image:
        returns : list of faces , image with bounding box on faces
        list of faces : are ready for input to the learning model just adjust the INPUT_SHAPE
    """
    detector = dlib.cnn_face_detection_model_v1('./important files/mmod_human_face_detector.dat')
#     detector = dlib.get_frontal_face_detector()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img)
    cropped_faces = []
    take = 7  # increase the size of the bounding box
    for face in faces:
        cropped_faces.append(img[ face.rect.top()-take :face.rect.bottom()+take, face.rect.left()-take:face.rect.right()+take , :].copy())
    for face in faces:
        cv2.rectangle(img,(face.rect.left()-5, face.rect.top()-5), (face.rect.right()+5, face.rect.bottom()+5) ,(0,255,0), 5)
    return cropped_faces , img


# This function is computationally less expensive and faster:
def face_detection_2(img):
    detector = dlib.get_frontal_face_detector()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img )
    cropped_faces = []
    take = 7  # increase the size of the bounding box
    for face in faces:
        cropped_faces.append(img[ face.top()-take :face.bottom()+take, face.left()-take:face.right()+take , :].copy())
    for face in faces:
        cv2.rectangle(img,(face.left()-5, face.top()-5), (face.right()+5, face.bottom()+5) ,(0,255,0), 5)
    return cropped_faces , img


# def face_detection_mtcnn(img_path):
#     img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
#     detector = MTCNN()
#     detections = detector.detect_faces(img)
#     img_with_dets = img.copy()
#     min_conf = 0.9
#     for det in detections:
#         if det['confidence'] >= min_conf:
#             x, y, width, height = det['box']
#             keypoints = det['keypoints']
#             cv2.rectangle(img_with_dets, (x,y), (x+width,y+height), (0,155,255), 3)
#             # cv2.circle(img_with_dets, (keypoints['left_eye']), 2, (0,155,255), 2)
#             # cv2.circle(img_with_dets, (keypoints['right_eye']), 2, (0,155,255), 2)
#             # cv2.circle(img_with_dets, (keypoints['nose']), 2, (0,155,255), 2)
#             # cv2.circle(img_with_dets, (keypoints['mouth_left']), 2, (0,155,255), 2)
#             # cv2.circle(img_with_dets, (keypoints['mouth_right']), 2, (0,155,255), 2)
#     plt.figure(figsize = (50,50))
#     plt.imshow(img_with_dets)
#     plt.axis('off')