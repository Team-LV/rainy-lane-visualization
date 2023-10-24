import numpy as np
import cv2
import time
import platform
import tflite_runtime.interpreter as tflite

from homomorphic import *
from fuzzyfilter import *
from LKD import *


EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]

def make_interpreter(model_file):
  model_file, *device = model_file.split('@')
  return tflite.Interpreter(
      model_path=model_file,
      experimental_delegates=[
          tflite.load_delegate(EDGETPU_SHARED_LIB,
                               {'device': device[0]} if device else {})
      ])

interpreter = tf.lite.Interpreter('model_full_integer_quant.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
#print(input_details)

output_details = interpreter.get_output_details()
#print(output_details)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failed')


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (512, 256))

    #flitering
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg = np.mean(gray)
    std = np.std(gray)
 
    s1=fuzzy_avg(avg)
    s2=fuzzy_std(std)
    sigma=filtersigma(s1,s2)
    
    fliter_img = homomorphic(frame, sigma[0], sigma[1])
    
    #input img to deep model            
    inp = fliter_img.astype(np.int32)
    inp = inp.astype(np.uint8)
    inp = inp[np.newaxis]

    interpreter.set_tensor(input_details[0]['index'],inp)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    output_data *= 255
    output_data = output_data.astype(np.int64)
    output_data = np.squeeze(output_data, axis=0)
    output_image = np.stack((output_data, output_data, output_data), axis=-1).astype(np.int32)
    
    #Calculating Lane Keeping Degree
    wrap_img, minv = wrapping(output_image)
    m = wrap_img.shape[1]//2 
    l,r,m=hist(wrap_img)
    d=distance(l,r,m)        
    window = slide_window_search(wrap_img,l,r)

    background = np.full((256, 1024, 3), 255, np.uint8)
    
    if (d < -0.28):
        cv2.putText(background,'WARNING_HARD LEFT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
        #print('hard left',-d)
    elif (d<-0.2):
        cv2.putText(background,'WARNING LEFT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(200,0,255),3)
        #print('left',-d)
    elif (d > 0.2):
        cv2.putText(background,'WARNING_RIGHT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(200,0,255),3)
        #print('right',d)
    elif (d > 0.28):
        cv2.putText(background,'WARNING_HARD RIGHT',(160,128),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
        #print('hard right',d)
    else:
        cv2.putText(background,' ',(200,128),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),6)
        #print('good')

    cv2.imshow('Alert', background)
    
    key = cv2.waitKey(20)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

