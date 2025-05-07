import numpy as np
import cv2

# haarcascade 분류기 파일 저장된 디렉토리 경로를 제공함
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 한글 경로에 파일을 읽지 못해 넘파이로 파일을 읽어옴
ff = np.fromfile(r'이미지.jpg', np.uint8)
# 넘파이에 이미지를 opencv 이미지로 불러온다
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지 크기조절 fx, fy 비율로 조절 1.0 원래의 크기로
# interpolation(보간법) : 이미지나 다른 데이터를 크기를 변경할 때 사용되는 방법
# INTER_LINEAR(양선형 보간법) 이미지 크기를 변경할 때 사용
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러개의 얼굴을 찾아, 감도, 이웃거리를 조절
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x, y, w, h) in faces:
    # 탐지된 얼굴 부분을 지운다
    face_img = img[y: y+h, x: x+w]
    # 이미지 축소
    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.1, fy=0.1)
    # 이미지 확대
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) # INTER_AREA : 이미지를 축소할 때 사용
    # 자른 이미지 확대한 이미지로 대체한다
    img[y: y + h, x: x + w] = face_img

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
