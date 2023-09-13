import cv2

def wrapping(img):
    source = np.float32([(80, 50), (240, 50), (1, 89), (319, 89)])
    destination = np.float32([(1, 1), (320, 1), (1, 240), (320, 240)])
    transform_matrix = cv2.getPerspectiveTransform(source, destination)
    minv = cv2.getPerspectiveTransform(destination, source)
    _img = cv2.warpPerspective(img, transform_matrix, (320, 240))
    return _img, minv

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
    meter_pix = 3.6/dist
    delta_d=(lane_mid-midpoint)*meter_pix
    if (delta_d < -1.3):
        print('hard left',-delta_d)
    elif (delta_d<-0.7):
        print('left',delta_d)
    elif (delta_d > 0.7):
        print('right',delta_d)
    elif (delta_d > 1.3):
        print('hard right',delta_d)
    else:
        print('good')
