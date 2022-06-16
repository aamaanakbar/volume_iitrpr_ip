import cv2
import utlis
 
###################################
path = '/home/cse-lab-207/Downloads/mob.jpg'
scale =2
wP = 300 *scale
hP= 400 *scale
###################################
 
while True:
    img = cv2.imread(path)
    img=cv2.resize(img,(0,0),None,0.45,0.45)
    #print(img)
    imgContours , conts = utlis.getContours(img,minArea=50000,filter=4)
    if len(conts) != 0:
        biggest = conts[0][2]
        print(biggest)
        imgWarp = utlis.warpImg(img, biggest, wP,hP)
        imgContours2, conts2 = utlis.getContours(imgWarp,
                                                 minArea=50000, filter=4,
                                                 cThr=[129,129],draw = False)
        if len(conts) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
                nPoints = utlis.reorder(obj[2])
                nW = round((utlis.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((utlis.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, '{}cm'.format(nW), (x + 100, y ), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (129, 0, 200), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x + 20, y +2 *h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (129, 0, 200), 2)
        cv2.imshow('object size from 30"cm" away. ', imgContours2)
        
 
    img = cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow('Original',img)
    cv2.waitKey(1)




