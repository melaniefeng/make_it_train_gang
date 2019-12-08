print("\n\nWelcome to controller\n")

password = ['0', '1', '2', '3']
passwordIndex = 0
errorCount = 0
prevGesture = -1

def process(predGesture):
    global password
    global passwordIndex
    global errorCount
    global prevGesture
    if passwordIndex == len(password):
        print('complete')
    else:
        nextGesture = password[passwordIndex]
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

keyFile = open('pwd.txt', 'r')
keyIn = keyFile.read().splitlines()

testInput = ['0', '0', '0', '1', '2', '1', '2', '3']
for i in testInput:
    process(i)
