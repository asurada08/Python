import numpy as np
import cv2  # openCV 라이브러리

ff = np.fromfile(r'이미지.jpg', np.uint8)  # 이미지를 읽어오기 바이너리로 넘파이에 저장
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)  # 이미지 디코딩
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지를 만화 스타일로 변환한다
cartoon_img = cv2.stylization(img, sigma_s=100,sigma_r=0.1)
# sigma_s : 이미지 공간 필터의 크기, sigma_r : 색상 필터의 크기

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)  # 사용자가 키를 누르면 닫힘
cv2.destroyAllWindows()  # openCV창 닫음
