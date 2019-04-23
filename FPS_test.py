import cv2 as cv
import numpy as np
import time

# Load the model
net = cv.dnn.readNet('MobileNetSSD/models/MobileNetSSD_deploy.caffemodel',
                     'MobileNetSSD/models/MobileNetSSD_deploy.prototxt')

# Specify target device
net.setPreferableBackend(cv.dnn.DNN_BACKEND_INFERENCE_ENGINE)
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)

# Read an image

img = cv.imread('/home/pi/004545.jpg')

# Prepare input blob and perform an inference
blob = cv.dnn.blobFromImage(img, size=(300, 300), ddepth=cv.CV_8U)
net.setInput(blob, scalefactor=1.0/127.5, mean=[127.5, 127.5, 127.5])

# Warmup
out = net.forward()

start = time.time()

numRuns = 100
for _ in range(numRuns):
  net.forward()

print('FPS: ', numRuns / (time.time() - start))
