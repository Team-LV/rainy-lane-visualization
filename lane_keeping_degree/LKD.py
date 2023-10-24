import numpy as np
import cv2


def wrapping(image):
    (h, w) = (image.shape[0], image.shape[1])
    # image 3~
    # source = np.float32([[544, 537], [814, 537], [476, 634], [1015, 634]])
    # rain_ternal
    source=np.float32([(165,79),(361,79),(14,211),(493,211)])
    destination = np.float32([(1,1),(1279,1),(150,719),(1100,719)])

    transform_matrix = cv2.getPerspectiveTransform(source, destination)
    minv = cv2.getPerspectiveTransform(destination, source)
    _image = cv2.warpPerspective(image, transform_matrix, (1280, 720))

    return _image, minv

def threshold(img):
    binary=250
    ret, img = cv2.threshold(img,binary,255,cv2.THRESH_BINARY)
    return ret, img

def hist(img):
    histogram = np.sum(img[img.shape[0]//2:,:],axis=0)
    midpoint = np.int16(histogram.shape[0]/2)
    l_base=np.argmax(histogram[:midpoint])
    r_base=np.argmax(histogram[midpoint:])+midpoint
    return l_base, r_base, midpoint

def distance(l_base, r_base, midpoint):
    dist = r_base-l_base
    lane_mid = l_base + dist * 0.5
    meter_pix = 0.04688*2
    delta_d=(lane_mid-midpoint)*meter_pix
    return delta_d

def slide_window_search(img, left_current, right_current):
    out_img = np.dstack((img,img,img))
    n= 1
    h= 360
    nonzero=img.nonzero()
    nonzero_y=np.array(nonzero[0])
    nonzero_x=np.array(nonzero[1])

    margin = 15
    minpix= 10
    left_lane = []
    right_lane= []
    color = [0,255,0]
    thickness = 1

    for w in range(n):

        win_y_low = img.shape[0] - (w+1)*h
        win_y_high = img.shape[0] - w*h
        win_xleft_low = left_current - margin
        win_xright_low = right_current - margin
        win_xleft_high = left_current + margin
        win_xright_high = right_current + margin

        cv2.rectangle(out_img, (win_xleft_low,win_y_low),(win_xleft_high,win_y_high),color,thickness)
        cv2.rectangle(out_img, (win_xright_low,win_y_low),(win_xright_high,win_y_high),color,thickness)
        good_left = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xleft_low) & (nonzero_x < win_xleft_high)).nonzero()[0]
        good_right = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xright_low) & (nonzero_x < win_xright_high)).nonzero()[0]

        left_lane.append(good_left)
        right_lane.append(good_right)

        if len(good_left) > minpix:
            left_current = np.int16(np.mean(nonzero_x[good_left]))

        if len(good_right) > minpix:
            right_current = np.int16(np.mean(nonzero_x[good_right]))

    left_lane = np.concatenate(left_lane)
    right_lane = np.concatenate(right_lane)

    leftx = nonzero_x[left_lane]
    lefty = nonzero_y[left_lane]
    rightx = nonzero_x[right_lane]
    righty = nonzero_y[right_lane]

    left_fit = np.polyfit(lefty,leftx,2)
    right_fit = np.polyfit(righty,rightx,2)

    y = np.linspace(0,img.shape[0]-1,img.shape[0])
    left_fitx = left_fit[0]*y**2 + left_fit[1]*y + left_fit[2]
    right_fitx = right_fit[0]*y**2 + right_fit[1]*y + right_fit[2]

    ltx = np.trunc(left_fitx)
    rtx = np.trunc(right_fitx)

    out_img[nonzero_y[left_lane], nonzero_x[left_lane]] = [255,0,0]
    out_img[nonzero_y[right_lane], nonzero_x[right_lane]] = [0,0,255]

    ret = {'leftx' : ltx, 'rightx' : rtx, 'y' : y}

    return ret


    out_img = np.dstack((img,img,img))
    n= 12
    h= 40
    nonzero=img.nonzero()
    nonzero_y=np.array(nonzero[0])
    nonzero_x=np.array(nonzero[1])

    margin = 20
    minpix= 5
    left_lane = []
    right_lane= []
    color = [0,255,0]
    thickness = 1

    for w in range(n):

        win_y_low = img.shape[0] - (w+1)*h
        win_y_high = img.shape[0] - w*h
        win_xleft_low = left_current - margin
        win_xright_low = right_current - margin
        win_xleft_high = left_current + margin
        win_xright_high = right_current + margin

        cv2.rectangle(out_img, (win_xleft_low,win_y_low),(win_xleft_high,win_y_high),color,thickness)
        cv2.rectangle(out_img, (win_xright_low,win_y_low),(win_xright_high,win_y_high),color,thickness)
        good_left = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xleft_low) & (nonzero_x < win_xleft_high)).nonzero()[0]
        good_right = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xright_low) & (nonzero_x < win_xright_high)).nonzero()[0]

        left_lane.append(good_left)
        right_lane.append(good_right)

        if len(good_left) > minpix:
            left_current = np.int16(np.mean(nonzero_x[good_left]))

        if len(good_right) > minpix:
            right_current = np.int16(np.mean(nonzero_x[good_right]))

    left_lane = np.concatenate(left_lane)
    right_lane = np.concatenate(right_lane)

    leftx = nonzero_x[left_lane]
    lefty = nonzero_y[left_lane]
    rightx = nonzero_x[right_lane]
    righty = nonzero_y[right_lane]

    left_fit = np.polyfit(lefty,leftx,2)
    right_fit = np.polyfit(righty,rightx,2)

    y = np.linspace(0,img.shape[0]-1,img.shape[0])
    left_fitx = left_fit[0]*y**2 + left_fit[1]*y + left_fit[2]
    right_fitx = right_fit[0]*y**2 + right_fit[1]*y + right_fit[2]

    ltx = np.trunc(left_fitx)
    rtx = np.trunc(right_fitx)

    out_img[nonzero_y[left_lane], nonzero_x[left_lane]] = [255,0,0]
    out_img[nonzero_y[right_lane], nonzero_x[right_lane]] = [0,0,255]

    ret = {'leftx' : ltx, 'rightx' : rtx, 'y' : y}

    return ret

def drawline(frame, img, minv, ret):
    left_fitx = ret['leftx']
    right_fitx = ret['rightx']
    y = ret['y']

    warp_zero = np.zeros_like(img).astype(np.uint8)
    color_warp = np.dstack((warp_zero,warp_zero,warp_zero))

    l = np.array([np.transpose(np.vstack([left_fitx,y]))])
    r = np.array([np.flipud(np.transpose(np.vstack([right_fitx,y])))])
    pts = np.hstack((l,r))

    mean_x = np.mean((left_fitx,right_fitx),axis=0)
    pts_mean = np.array([np.flipud(np.transpose(np.vstack([mean_x,y])))])

    cv2.fillPoly(color_warp, np.int_([pts]),(0,0,255))
    cv2.fillPoly(color_warp, np.int_([pts_mean]), (0, 0, 255))


    newwarp = cv2.warpPerspective(color_warp, minv, (frame.shape[1], frame.shape[0]))
    result = cv2.addWeighted(frame,1,newwarp,0.7,0.0,dtype=cv2.CV_8U)


    return result



    img = np.full((256, 1024, 3), 255, np.uint8)

    if (d < -1.3):
        cv2.putText(img,'WARNING_HARD LEFT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
        #print('hard left',-d)
    elif (d<-0.7):
        cv2.putText(img,'WARNING LEFT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(200,0,255),3)
        #print('left',-d)
    elif (d > 0.7):
        cv2.putText(img,'WARNING_RIGHT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(200,0,255),3)
        #print('right',d)
    elif (d > 1.3):
        cv2.putText(img,'WARNING_HARD RIGHT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
        #print('hard right',d)
    else:
        cv2.putText(img,' ',(160,128),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),6)
        #print('good')

    return img
