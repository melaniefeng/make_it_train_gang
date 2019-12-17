
# coding: utf-8

# In[21]:


print("\n\nWelcome to controller\n")

password = []
passwordIndex = 0
errorCount = 0
prevGesture = -1

def unlock(predList):
    print('unlock updated')
    global password
    global passwordIndex
    global errorCount
    global prevGesture
    print(predList)
    predGesture = predList[0]
    print(predGesture)
    if passwordIndex == len(password):
        print('complete')
    else:
        nextGesture = password[passwordIndex]
        print(nextGesture)
        if predGesture == nextGesture:
            passwordIndex = passwordIndex + 1
            prevGesture = password[passwordIndex - 1]
            if passwordIndex == len(password):
                print('opened')
                reset()
                return True
        elif not predGesture == prevGesture:
            if passwordIndex != 0:
                errorCount = errorCount + 1
            print('incorrect')
            if errorCount > 2:
                return False
                reset()
    return True
        
def reset():
    global password
    global passwordIndex
    global errorCount
    global prevGesture
    print('reset')
    passwordIndex = 0
    errorCount = 0
    prevGesture = -1

def setPassword(predList):
    print('setting password')
    global password
    global passwordIndex
    global errorCount
    global prevGesture
    
    predGesture = predList[0]
    print('current gesture', predGesture)
    #password length of 4
    

    
    pastGesture = 0
    
    if passwordIndex == 0:
        open("pwd.txt", "w").close()
    
    else:
        pastGesture = password[passwordIndex]

    if not predGesture == pastGesture:
        password.append(predGesture)
        line = ' '.join(str(e) for e in predList)
        line = line + '\n'
        print(line)
        keyFile = open("pwd.txt", "a")
        keyFile.write(line)
        keyFile.close()

    passwordIndex = passwordIndex + 1
    if passwordIndex == 4:
        print('password set')
        reset()
        return True
    return False
        
def initPassword():
    global password
    keyFile = open('pwd.txt', 'r')
    passwordLoc = keyFile.read().splitlines()
    password = []
    for c in passwordLoc:
        d = c.split(" ")
        password.append(d[0])

#def initPassword():
#    global password
#    keyFile = open('pwd.txt', 'r')
#    password = keyFile.read().splitlines()

