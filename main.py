import cv2
from retinex import MSR
from image_processing import wrapping, threshold, hist, distance

variance_list = [15, 40, 80]

cap = cv2.VideoCapture('eTest1.mp4')

if not cap.isOpened():
    print('Failed')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(320,240))
    frame = frame[151:240,1:320]
    
    #cv2.imshow('org',frame)
    if not ret:
        break
    
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    MSR_img=MSR(frame,variance_list)
    MSR_img,minv=wrapping(MSR_img)
    MSR_img = cv2.cvtColor(MSR_img,cv2.COLOR_BGR2GRAY)
    value, MSR_img = threshold(MSR_img)
    l,r,m=hist(MSR_img)
    distance(l,r,m)
    
    cv2.imshow('frame',MSR_img)
    
    key = cv2.waitKey(20)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
