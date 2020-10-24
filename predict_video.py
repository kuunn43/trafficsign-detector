import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np
import time
import xlsxwriter
import pandas as pd

#load video
cap = cv2.VideoCapture('E:/KUN/TA/darkflow-master/Uji/videouji/stop1.2.mp4')

#get total frame in video
totalFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(totalFrame)

#load model
options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 15000,
    'gpu': 0.7
    }

tfnet = TFNet(options)
colors=[tuple(255 * np.random.rand(3)) for i in range(5)]
out = cv2.VideoWriter('hasil_prediksi.avi',cv2.VideoWriter_fourcc(*'MJPG'),30, (640,480))
predicted_counter = 0
while(cap.isOpened()):
    stime= time.time()
    ret, frame = cap.read()
    if ret:
        results = tfnet.return_predict(frame)
        label = 'not detected'
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame= cv2.rectangle(frame, tl, br, color, 2)
            frame= cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 1)

            if label == 'kanan' or label == 'kiri': #if false prediction
                break            
        out.write(frame)
        cv2.imshow('frame', frame)

        if label == 'stop':
            predicted_counter +=1

        if cv2.waitKey(1)  & 0xFF == ord('q'):
            break
    else:
        break

akurasi = (predicted_counter/totalFrame)*100

print('total frame : ',totalFrame)
print('rambu diprediksi : ',predicted_counter)
print('akurasi (%) :',akurasi)

cap.release()
out.release()
cv2.destroyAllWindows()