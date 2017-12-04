from inputs import get_gamepad
import pyautogui

speed = 100
while 1:
    events = get_gamepad()
    for event in events:
        #Croix directionnelle
        if (event.code == "ABS_HAT0Y" and event.state == -1):
            pyautogui.moveRel(0, -speed, duration=0)
        elif (event.code == "ABS_HAT0Y" and event.state == 1):
            pyautogui.moveRel(0, speed, duration=0)
        elif (event.code == "ABS_HAT0X" and event.state == 1):
            pyautogui.moveRel(speed, 0, duration=0)
        elif (event.code == "ABS_HAT0X" and event.state == -1):
            pyautogui.moveRel(-speed, 0, duration=0)
        #Analog left
        if (event.code == "ABS_Y" and event.state <= -10000):
            pyautogui.moveRel(0, speed, duration=0)
        elif (event.code == "ABS_Y" and event.state >= 10000):
            pyautogui.moveRel(0, -speed, duration=0)
        elif (event.code == "ABS_X" and event.state >= 10000):
            pyautogui.moveRel(speed, 0, duration=0)
        elif (event.code == "ABS_X" and event.state <= -10000):
            pyautogui.moveRel(-speed, 0, duration=0)
        #A,B,Y and X
        elif (event.code == "BTN_SOUTH" and event.state == 1):
            pyautogui.click()
        elif (event.code == "BTN_EAST" and event.state == 1):
            pyautogui.click(button="right")
        elif (event.code == "BTN_NORTH" and event.state == 1):
            if (speed < 100):
                speed *= 10
        elif (event.code == "BTN_WEST" and event.state == 1):
            if (speed > 1):
                speed /= 10
