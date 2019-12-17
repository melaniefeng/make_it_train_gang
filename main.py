
# coding: utf-8

# In[4]:


import subprocess
import os
from parse import PredictionParser
import wget
import controller_location
import playVideo
import controller


# In[5]:


import imp
imp.reload(controller)
controller.reset()
testInput = [['longhorn', 0, 200], ['longhorn', 0, 200], ['L', 100, 1000],['L', 100, 1000],['L', 100, 1000], ['palm', 50, 900]]

for i in testInput:
    print("here", i)
    controller.unlock(i)


# In[6]:


controller.initPassword()
print(controller.password)
threshold = .3


# In[ ]:


controller.reset()
controller.initPassword()
print(controller.password)
count = 0
while(True):
    img_name = str(count)+'.jpg'
    print('request')
    subprocess.Popen(['wget', '-q' ,'-O', img_name, 'http://192.168.1.33:8000/shot.jpg']).wait()
    print('picture obtained')
    output = subprocess.Popen(['./darknet','detector', 'test', 'cfg/data3.data','cfg/yolo_data3.cfg', 'yolo-obj_13000.weights', img_name, '-thresh', '.1'], stdout = subprocess.PIPE)
    results = PredictionParser().parse_preds(output.communicate()[0], threshold)
    print(results)
    if len(results) > 0:
        query = [results[0]['class'], int(results[0]['coords'][0][0]), int(results[0]['coords'][0][1])]
        print(query)
        controller.unlock(query)
           
    count = count + 1

