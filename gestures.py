import mediapipe as mp

def classify_gesture(hand_landmarks):
    finger_states = []
    tips = [4, 8, 12, 16, 20]
    pip_joints = [2, 6, 10, 14, 18]

    for tip, pip in zip(tips, pip_joints):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            finger_states.append(1)
        else:
            finger_states.append(0)

    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        finger_states[0] = 1
    else:
        finger_states[0] = 0

    if finger_states == [1, 1, 1, 1, 1]:
        return "Play"
    elif finger_states == [0, 0, 0, 0, 0]:
        return "Pause"
    elif finger_states == [0, 1, 1, 0, 0]:
        return "Volume Up"
    elif finger_states == [0, 0, 1, 1, 0]: 
        return "Volume Down"
    elif finger_states == [1, 0, 0, 0, 0]:
        return "Next"
    elif finger_states == [0, 1, 1, 1, 1]:
        return "Previous"
    else:
        return "Unknown"
