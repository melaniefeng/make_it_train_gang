import cv2


def playVideo():
    cap = cv2.VideoCapture('openDoor.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            # & 0xFF is required for a 64-bit system
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

playVideo()