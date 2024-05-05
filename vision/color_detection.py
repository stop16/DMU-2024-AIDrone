import cv2

# Initialize the OpenCV video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Adjust saturation of the source image
    saturation = 5.2
    hsv_frame[:,:,1] = (hsv_frame[:,:,1] * saturation) # 0은 Hue, 1은 Saturation, 2는 Value

    # Display the adjusted HSV image
    rgb_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('HSV Frame', rgb_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and exit
cap.release()
cv2.destroyAllWindows()
