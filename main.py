import math
import cv2
import mediapipe as mp
import pyfirmata2 as firm
import serial
import time
arduino = serial.Serial("COM4",9600)
time.sleep(2)
# board = firm.Arduino("COM4")
# it = firm.util.Iterator(board)
# it.start()
# lightPin = board.get_pin("d:2:o")
# lightPin1 = board.get_pin("d:3:o")
# lightPin2 = board.get_pin("d:4:o")
# lightPin3 = board.get_pin("d:5:o")
# lightPin4 = board.get_pin("d:6:o")
# lightPin5 = board.get_pin("d:7:o")
# ir_pin = board.get_pin("d:8:i")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2,model_complexity=1)
mp_handedness = mp.solutions.hands.Hands

while(True):
    success , frame = cap.read()
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        print(f"IR Sensor Reading: {data}")

        # تقدر تستخدم القراءة هنا مثلا:
        if data == "1":
            print("Object Detected!")
        elif data == "0":
            print("No Object.")
    if(success):
        RGB_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(RGB_frame)

        if (results.multi_hand_landmarks): #
            # if(len(results.multi_hand_landmarks) == 1):
            for idx,hand_land_mark in enumerate(results.multi_hand_landmarks): #
                hand_label = results.multi_handedness[idx].classification[0].label #
                mp_drawing.draw_landmarks(frame,hand_land_mark,
                                          mp_hands.HAND_CONNECTIONS,)
                indexTip = hand_land_mark.landmark[4]
                thumbTip = hand_land_mark.landmark[17]
                x = (indexTip.x-thumbTip.x)**2
                y = (indexTip.y-thumbTip.y)**2

                distance = math.sqrt(x+y)
                
                indexTip2 = hand_land_mark.landmark[8]
                thumbTip2 = hand_land_mark.landmark[5]
                x2 = (indexTip2.x-thumbTip2.x)**2
                y2 = (indexTip2.y-thumbTip2.y)**2

                distance2 = math.sqrt(x2+y2)
                
                indexTip3 = hand_land_mark.landmark[12]
                thumbTip3 = hand_land_mark.landmark[9]
                x3 = (indexTip3.x-thumbTip3.x)**2
                y3 = (indexTip3.y-thumbTip3.y)**2

                distance3 = math.sqrt(x3+y3)
                
                indexTip4 = hand_land_mark.landmark[16]
                thumbTip4 = hand_land_mark.landmark[13]
                x4 = (indexTip4.x-thumbTip4.x)**2
                y4 = (indexTip4.y-thumbTip4.y)**2

                distance4 = math.sqrt(x4+y4)
                
                indexTip5 = hand_land_mark.landmark[20]
                thumbTip5 = hand_land_mark.landmark[17]
                x5 = (indexTip5.x-thumbTip5.x)**2
                y5 = (indexTip5.y-thumbTip5.y)**2

                distance5 = math.sqrt(x5+y5)

                if hand_label == "Right":
                    hand_label = "Left"
                elif hand_label == "Left":
                    hand_label = "Right"
                print(f"{hand_label} hand distance first finger: {round(distance,2)}")
                print(f"{hand_label} hand distance second finger: {round(distance2,2)}")
                print(f"{hand_label} hand distance third finger: {round(distance3,2)}")
                print(f"{hand_label} hand distance forth finger: {round(distance4,2)}")
                print(f"{hand_label} hand distance fifth finger: {round(distance5,2)}")

                if hand_label == "Right":
                    print("")
                    # lightPin1.write(1 if distance>0.15 else 0)
                    # lightPin2.write(1 if distance2>0.15 else 0)
                    # lightPin3.write(1 if distance3>0.15 else 0)
                    # lightPin4.write(1 if distance4>0.15 else 0)
                    # lightPin5.write(1 if distance5>0.15 else 0)
                elif(hand_label == "Left"):
                    print("")
                    # lightPin.write(1 if distance2>0.15 else 0)

                # if(hand_label == "Right"):
                #     cv2.line(frame,pt1=(int(indexTip.x * frame.shape[1]), int(indexTip.y * frame.shape[0])),pt2=(int(thumbTip.x * frame.shape[1]),int(thumbTip.y * frame.shape[0])),color=(255,0,0),thickness=3)
                # elif(hand_label == "Left"):
                #     cv2.line(frame,pt1=(int(indexTip.x * frame.shape[1]), int(indexTip.y * frame.shape[0])),pt2=(int(thumbTip.x * frame.shape[1]),int(thumbTip.y * frame.shape[0])),color=(255,0,255),thickness=3)

           
        frame = cv2.flip(frame,1)
        cv2.imshow("THE CAMARA",frame)
        if cv2.waitKey(1) == ord("q"):
            break
# cv2.destroyAllWindows()
# import matplotlib.pyplot as plt
# Mostafa = cv2.imread("Mostafa.png")
# After_Modify = cv2.cvtColor(Mostafa,cv2.COLOR_BGR2RGB)
# cv2.imshow("Mostafa",cv2.resize(Mostafa,(500,500)))
# plt.subplot(2,1,1)
# plt.imshow(Mostafa)
# plt.axis("off")
# plt.subplot(2,2,1)
# plt.imshow(After_Modify)
# plt.axis("off")
# plt.show()
