print("\n\nWelcome to controller\n")

password = None
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
        elif not predGesture == prevGesture:
            if passwordIndex != 0:
                errorCount = errorCount + 1
            print('incorrect')
            if errorCount > 5:
                reset()
        
def reset():
    global password
    global passwordIndex
    global errorCount
    global prevGesture
    print('reset')
    passwordIndex = 0
    errorCount = 0
    prevGesture = -1

def setPassword():
    pass
    #read pfrom sean script
    
    #write to password.txt array
    #hold out hand
    #take10 pic

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

initPassword()
testInput = ['0', '0', '0', '1', '2', '1', '2', '3']
for i in testInput:
    unlock(i)
