
# coding: utf-8

# In[48]:


import subprocess
import os
from parse import PredictionParser

import controller_location


# In[51]:


import imp
imp.reload(controller_location)
print(controller_location.passwordLoc)
controller_location.reset()
testInput = [['cat', 0, 200], ['bird', 100, 1000], ['bird', 50, 900]]

for i in testInput:
    controller_location.unlock(i)


# In[32]:


threshold = .6


# In[25]:


password = []
for c in controller.password:
    d = c.split(" ")
    passwordID.append(d[0])
    d[1] = int(d[1])
    d[2] = int(d[2])
    password.append(d)

print(password)


# In[52]:


controller_location.reset()
print(controller_location.password)
for filename in os.listdir('input_images'):
    img = 'input_images/' + filename
    output = subprocess.Popen(['./darknet', 'detect', 'cfg/yolov2.cfg', 'yolov2.weights', img], stdout = subprocess.PIPE)
    results = PredictionParser().parse_preds(output.communicate()[0], threshold)
    print(results)
    if len(results) > 0:
        query = [results[0]['class'], int(results[0]['coords'][0][0]), int(results[0]['coords'][0][1])]
        print(query)
        controller_location.unlock(query)

