# coding: utf-8

print("\n\nWelcome to controller\n")

def sign(num):
    if num == 0:
        return 0
    elif num < 0:
        return -1
    else:
        return 1

password = None
passwordIndex = 0
errorCount = 0
prevGesture = [-1, -1, -1]
prevInputGesture = [-1, -1, -1]
passwordLoc = None
def unlock(predGesture):
    global passwordLoc
    global passwordIndex
    global errorCount
    global prevGesture
    global prevInputGesture
    if passwordIndex == len(password):
        print('complete')
    else:
            
        nextGesture = passwordLoc[passwordIndex][0]
        nextGestureUL_x = passwordLoc[passwordIndex][1]
        nextGestureUL_y = passwordLoc[passwordIndex][2]
        print(passwordLoc[passwordIndex])
      
        shiftCheck = False
        shiftDir = False
        if prevInputGesture[0] == -1 or prevGesture[0] == -1:
            prevInputGesture = predGesture
            shiftCheck = True
            shiftDir = True
        else:
            expShift_x = prevGesture[1]-nextGestureUL_x
            expShift_y = prevGesture[2]-nextGestureUL_y
            
            print('expected shift', expShift_x, expShift_y)
            currShift_x = prevInputGesture[1]-predGesture[1]
            currShift_y = prevInputGesture[2]-predGesture[2]
            print('current shift', currShift_x, currShift_y)
            
            if sign(expShift_x) == sign(currShift_x):
                if sign(expShift_y) == sign(currShift_y):
                    print('shiftDir')
                    shiftDir = True
            #threshold to check if movement is okay
            if currShift_x <= expShift_x+abs(expShift_x)*.1 and currShift_x >= expShift_x-abs(expShift_x)*.1:
                print('threshold:',abs(expShift_x)*.1)
                print('UL ok')
                if currShift_y <= expShift_y+abs(expShift_y)*.1 and currShift_y >= expShift_y-abs(expShift_y)*.1:
                    print('BR ok')
                    shiftCheck = True
                
        if predGesture[0] == nextGesture and shiftCheck:
            #gesture ID matches, check relative location
            print('check1', predGesture)
            prevGesture = passwordLoc[passwordIndex]
            prevInputGesture = predGesture
            passwordIndex = passwordIndex + 1
            if passwordIndex == len(password):
                print('opened')
                reset()
                
        elif not predGesture[0] == prevGesture[0] or not shiftDir:
            if passwordIndex != 0:
                errorCount = errorCount + 1
            print('incorrect')
            if errorCount > 5:
                reset()
        
def reset():
    global passwordIndex
    global errorCount
    global prevGesture
    global prevInputGesture
    print('reset')
    passwordIndex = 0
    errorCount = 0
    prevGesture = [-1, -1, -1]
    prevInputGesture = [-1, -1, -1]

def setPassword():
    pass
    #read pfrom sean script
    
    #write to password.txt array
    #hold out hand
    #take10 pic

def initPassword():
    global password
    global passwordLoc
    keyFile = open('pwd.txt', 'r')
    password = keyFile.read().splitlines()
    passwordLoc = []
    for c in password:
        d = c.split(" ")
        d[1] = int(d[1])
        d[2] = int(d[2])
        passwordLoc.append(d)
    print(passwordLoc)


initPassword()
testInput = [['cat', 0, 200], ['bird', 50, 1000], ['bird', 0, 900]]

for i in testInput:
    unlock(i)

