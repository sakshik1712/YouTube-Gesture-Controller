import cv2
import mediapipe as mp
from gestures import classify_gesture
from utils import can_trigger
from browser_control import YouTubeController

yt = YouTubeController()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    gesture = "No Hand"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = classify_gesture(hand_landmarks)

            if can_trigger(gesture):
                print(f"Gesture detected: {gesture}")
                if gesture == "Play":
                    yt.play()
                elif gesture == "Pause":
                    yt.pause()
                elif gesture == "Volume Up":
                    yt.volume_up()
                elif gesture == "Volume Down":
                    yt.volume_down()
                elif gesture == "Next":
                    yt.next_video()
                elif gesture == "Previous":
                    yt.previous_video()

    cv2.putText(img, f'Gesture: {gesture}', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("YouTube Gesture Controller", img)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()