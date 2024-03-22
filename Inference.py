import cv2
import mediapipe as mp
import numpy as np
from keras.models import load_model
import time
import pyautogui

def inference():
    model = load_model('model.h5')
    label = np.load('labels.npy')

    holistic = mp.solutions.holistic
    hands = mp.solutions.hands
    holis = holistic.Holistic()
    drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while True:
        lst = []
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.pose_landmarks:
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                lst.extend([0.0] * 42)

            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                lst.extend([0.0] * 42)
        else:
            # If no pose landmarks are detected, fill lst with zeros
            lst.extend([0.0] * 84)

        lst = np.array(lst).reshape(1, -1)

        pred = label[np.argmax(model.predict(lst))]
        print(pred)

        cv2.imshow("window", frm)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break


