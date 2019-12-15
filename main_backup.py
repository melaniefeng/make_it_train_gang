
# coding: utf-8

# In[28]:


import subprocess
import os
from parse import PredictionParser
import wget
import controller_location
import controller


# In[44]:


import imp
imp.reload(controller)
controller.reset()
testInput = [['longhorn', 0, 200], ['longhorn', 0, 200], ['L', 100, 1000],['L', 100, 1000],['L', 100, 1000], ['palm', 50, 900]]

for i in testInput:
    print("here", i)
    controller.unlock(i)


# In[29]:


controller.initPassword()
print(controller.password)
threshold = .8


# In[45]:


controller.reset()
controller.initPassword()
print(controller.password)
count = 0
while(True):
    img_name = str(count)+'.jpg'
    print('request')
    subprocess.Popen(['wget', '-q' ,'-O', img_name, 'http://10.147.45.42:8000/shot.jpg']).wait()
    print('picture obtained')
    output = subprocess.Popen(['./darknet','detector', 'test', 'cfg/voc.data','cfg/yolo-gesture.cfg', 'yolo-obj_16000.weights', img_name], stdout = subprocess.PIPE)
    results = PredictionParser().parse_preds(output.communicate()[0], threshold)
    print(results)
    if len(results) > 0:
        query = [results[0]['class'], int(results[0]['coords'][0][0]), int(results[0]['coords'][0][1])]
        print(query)
        controller.unlock(query)
    count = count + 1

