import mediapipe as mp
import numpy as np
import cv2

def datacollection(value):
    holistic=mp.solutions.holistic
    hands=mp.solutions.hands
    holis=holistic.Holistic()
    drawing=mp.solutions.drawing_utils


    name = value

    #video input
    cap=cv2.VideoCapture(0)

    x1=[]
    data_size = 0
    # x2=[]

    while True:
        lst=[]
        #read the contents of the video in frames
        _,frame=cap.read()
        frame=cv2.flip(frame,1)  #just flip the pic (not necessary)

        res=holis.process(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        if res.right_hand_landmarks:
            for i in res.right_hand_landmarks.landmark:
                lst.append(i.x-res.right_hand_landmarks.landmark[8].x)
                lst.append(i.y-res.right_hand_landmarks.landmark[8].y)
        else:
            for _ in range(21):
                lst.extend([0.0,0.0])

        
        x1.append(lst)
        data_size+=1

        if res.left_hand_landmarks:
            for i in res.left_hand_landmarks.landmark:
                lst.append(i.x-res.left_hand_landmarks.landmark[8].x)
                lst.append(i.y-res.left_hand_landmarks.landmark[8].y)
        else:
            for _ in range(21):
                lst.extend([0.0,0.0])

        
        x1.append(lst)
        data_size+=1
        

        
        drawing.draw_landmarks(frame,res.right_hand_landmarks,hands.HAND_CONNECTIONS)  #used to mark the points on the frame
        drawing.draw_landmarks(frame,res.left_hand_landmarks,hands.HAND_CONNECTIONS)  #used to mark the points on the frame
        cv2.putText(frame, str(data_size), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("window",frame)  #to show us what is capturing
        #to stop the cam capturing
        if cv2.waitKey(1)==27 or data_size>99:
            cap.release()
            cv2.destroyAllWindows()
            break

    np.save(f"{name}.npy",np.array(x1))
    # np.save(f"{name}.npy",np.array(x2))
    print(np.array(x1).shape)
    # print(np.array(x2).shape)