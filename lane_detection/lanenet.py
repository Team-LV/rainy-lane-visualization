import numpy as np
import cv2
import time
import platform
import tflite_runtime.interpreter as tflite

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

interpreter = tf.lite.Interpreter('model_full_integer_quant.tflite',)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
#print(input_details)

output_details = interpreter.get_output_details()
#print(output_details)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Failed')

fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (512, 256))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (512, 256))
            
    inp=frame.astype(np.int32)
    inp = inp.astype(np.uint8)
    inp = inp[np.newaxis]

    interpreter.set_tensor(input_details[0]['index'],inp)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    output_data *= 255
    output_data = output_data.astype(np.int64)
    output_data = np.squeeze(output_data, axis=0)
    output_image = np.stack((output_data, output_data, output_data), axis=-1).astype(np.int32)
    
    out.write(output_image)

    cv2.imshow('frame', output_image)
    key = cv2.waitKey(20)
    if key == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

