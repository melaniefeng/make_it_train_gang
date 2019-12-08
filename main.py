
# coding: utf-8

# In[1]:


import subprocess
import os
from parse import PredictionParser
import controller


# In[4]:


threshold = .6
controller.initPassword()
print(controller.password)
for filename in os.listdir('input_images'):
    img = 'input_images/' + filename
    output = subprocess.Popen(['./darknet', 'detect', 'cfg/yolov2.cfg', 'yolov2.weights', img], stdout = subprocess.PIPE)
    results = PredictionParser().parse_preds(output.communicate()[0], threshold)
    print(results)
    if len(results) > 0:
        controller.unlock(results[0]['class'])

