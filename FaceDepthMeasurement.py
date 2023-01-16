import cv2
import cvzone

import FaceMeshModule as fmm
from cvzone.FaceMeshModule import FaceMeshDetector

# wCam, hCam = 1280,720

cap = cv2.VideoCapture(0)
# cap.set(3,wCam)
# cap.set(4,hCam)

detector = FaceMeshDetector(maxFaces=1)  #if you are using module created by you use detector = fmm.FaceMeshDetector()

while True:
    success, img = cap.read()
    img,faces = detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        w,_= detector.findDistance(pointLeft,pointRight) # you can use distance formula here
        W = 6.3

        #finding the focal length

                 #cm Avg Value for male is 6.4 and female 6.2
        # d = 50
        # f =(w*d)/W
        #
        # print(f)

        # finding distance
        f = 840
        d = (W*f)/w
        print(d)


        cvzone.putTextRect(img,f'Depth: {int(d)}cm',
                           (face[10][0]-100,face[10][1]-50),
                           scale=2)

    cv2.imshow("img",img)
    cv2.waitKey(1)