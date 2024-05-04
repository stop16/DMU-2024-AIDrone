# OpenCV 사용해서 웹캠을 창에 띄우는 예제

import cv2
cap = cv2.VideoCapture(0)  # 0: 웹캠 인덱스 (기본)
while True: # 웹캠이 켜져있는 동안 반복할 Loop
    ret, frame = cap.read() # 카메라로부터 이미지 읽어오기
    if not ret: # 카메라 읽어오기 실패하면 종료
        break
    cv2.imshow('Webcam', frame) # 웹캠 이미지 창에 띄우기
    if cv2.waitKey(1) & 0xFF == ord('q'): # q: 종료
        break

cap.release() # 카메라 해제
cv2.destroyAllWindows() # 웹캠 창 닫기