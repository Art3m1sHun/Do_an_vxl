import cv2
import mediapipe as mp
import time
import main

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.75)
mp_drawing = mp.solutions.drawing_utils

# Video Capture
cap = cv2.VideoCapture(0)

# Danh sách các chỉ số của các đầu ngón tay
tipIds = [4, 8, 12, 16, 20]

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Không lấy được frame từ camera.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    fingers = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lmList = []
            h, w, c = img.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                # Kiểm tra ngón cái (thumb)
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  # Đối với tay phải
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Kiểm tra 4 ngón còn lại
                for i in range(1, 5):
                    if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                totalFingers = fingers.count(1)

                # Hiển thị số ngón tay
                cv2.putText(img, f'Fingers: {totalFingers}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 4)
                print("Số ngón tay:", totalFingers)
                settings = []
                if(totalFingers == 1):
                    main.serialwritedata('01')
                elif(totalFingers == 2):
                    main.serialwritedata('02') 
                elif(totalFingers == 3):
                    main.serialwritedata('03')
                elif(totalFingers == 4):
                    main.serialwritedata('04')
                elif(totalFingers == 5):
                    main.serialwritedata('05')
                elif(totalFingers == 0):
                    main.serialwritedata('00')

    # Hiển thị thời gian
    text = f"time: {time.strftime('%H:%M:%S')}"
    cv2.putText(img, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Finger Counter", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
