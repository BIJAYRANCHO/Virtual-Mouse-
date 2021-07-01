import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id % 4==0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)                 

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                # ID 4 less than 3 in x axis , "thumb is down"
                # ID 8 less than 5 in y axis , "Index is down"    
                # ID 12 less than 9 in y axis , "Midle is down"    
                # ID 16 less than 13 in y axis , "Ring is down"    
                # ID 20 less than 17 in y axis , "pinki is down"   
            thumbFingerIsOpen = False
            indexFingerIsOpen = False
            midleFingerIsOpen = False
            ringFingerIsOpen = False
            pinkiFingerIsOpen = False

            pseudoFixKeyPoint = landmarkList.landmark(2).x();
            if (landmarkList.landmark(3).x() < pseudoFixKeyPoint and landmarkList.landmark(4).x() < pseudoFixKeyPoint):
                    thumbIsOpen = True;
                    if thumbIsOpen == True:
                        print("thumb is up")
                        

            pseudoFixKeyPoint = landmarkList.landmark(6).y();
            if (landmarkList.landmark(7).y() < pseudoFixKeyPoint and landmarkList.landmark(8).y() < pseudoFixKeyPoint):
                
                    indexFingerIsOpen = True;
                    if indexIsOpen == True:
                        print("index is up")

            pseudoFixKeyPoint = landmarkList.landmark(10).y();
            if (landmarkList.landmark(11).y() < pseudoFixKeyPoint and landmarkList.landmark(12).y() < pseudoFixKeyPoint):
                
                    midleFingerIsOpen = True;
                    if midleIsOpen == True:
                        print("midle is up")
                

            pseudoFixKeyPoint = landmarkList.landmark(14).y();
            if (landmarkList.landmark(15).y() < pseudoFixKeyPoint and landmarkList.landmark(16).y() < pseudoFixKeyPoint):
                
                    ringFingerIsOpen = True;
                    if ringIsOpen == True:
                        print("ring is up")
                

            pseudoFixKeyPoint = landmarkList.landmark(18).y();
            if (landmarkList.landmark(19).y() < pseudoFixKeyPoint and landmarkList.landmark(20).y() < pseudoFixKeyPoint):
                
                    pinkiFingerIsOpen = True;
                    if pinkiFingerIsOpen == True:
                        print("pinki is up")
                

                # If index and Middle is up . trigger mouse  
                

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)