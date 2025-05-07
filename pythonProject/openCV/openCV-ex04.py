import numpy as np
import cv2

ff = np.fromfile(r'이미지.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지 원 크기 1, 1
img = cv2.resize(img, dsize=(0, 0), fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)


def onchange(pos):
    pass


cv2.namedWindow("Trackbar Windows")  # Trackbar에 추가할 윈도우 이름 생성

# sigma_s = sigma_r 두 값을 조절하여 값이 변화 때마다 사진에 적용
cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onchange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onchange)
# sigma_s 초기 값을 100으로 저장
cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

while True:
    if cv2.waitKey(100) == ord('q'):  # 100밀리초 후에 q가 들어오면 빠짐
        break

    # 트랙바에서 sigma_s값 읽어오기
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    # 트랙바에서 sigma_r값 읽어오기 / 100으로 나누어 실제 값으로 변환
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    print("sigma_s_value :", sigma_s_value)
    print("sigma_r_value :", sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)

    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows()
