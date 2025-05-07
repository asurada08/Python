import numpy as np
import cv2

# 얼굴과 눈을 찾기위한 OpenCV 알고리즘이 적용된 파일을 불러온다
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 한글 경로에 파일을 읽지 못해 넘파이로 파일을 읽어옴
ff = np.fromfile(r'이미지.png', np.uint8)
# 넘파이에 이미지를 opencv 이미지로 불러온다
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지 크기조절 fx, fy 비율로 조절 1.0 원래의 크기로
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러개의 얼굴을 찾아, 감도, 이웃거리를 조절
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # 얼굴을 찾아 파란색 네모로 표시
    for (ex, ey, ew, eh) in eyes:  # 눈을 찾아 녹색 네모로 표시
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
