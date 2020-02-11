from pynput.keyboard import Key, Controller
import time
import random
wait=5             #Time you need between running the program and selecting the faculty

while(wait>0):
    print("Select within:",wait,"Seconds")
    time.sleep(1)
    wait-=1

keyboard=Controller()
time.sleep(1)
for i in range(18):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(random.randint(1,5)):
        keyboard.press(Key.left)
        keyboard.release(Key.left)


