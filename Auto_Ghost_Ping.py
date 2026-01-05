# PROGRAM: Auto ghost pinger
# This program ghost ping repeatedly on discord!
# Recommended to use the python terminal

# DEKLARASI - Library
import keyboard 
import pyautogui
import time
import sys

# DEKLARASI - Variable
active = False

# DEKLARASI - Subprogram
def toggle_on():
    global active
    active = True
    print(f"Activated! Will ghost ping {ping} repeatedly.")

def toggle_off():
    global active
    active = False
    print("Stop!")

def addname():
    global ping
    ping = input("please input the name of ur target for example @someone : ")

def end_program():
    print("Program ended")
    sys.exit()
    
#algoritma
if __name__ == "__main__":

    #input program
    ping = input("please input the name of ur target for example @someone : ")
    print("PRESS F11 first for full screen or else it didnt work")
    print("Press F4 to activate, F2 to deactivate, F to rename, ESC to end program.")
    
    # BIND KEYS
    keyboard.add_hotkey('F4', toggle_on)
    keyboard.add_hotkey('F2', toggle_off)
    keyboard.add_hotkey("F", addname)
    keyboard.add_hotkey('esc', end_program)

    #proses program
    try:
        while True:
            if active:
                pyautogui.typewrite(f'{ping}\n')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('up')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(0.1)
                pyautogui.press('backspace')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(2)
            else:
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("Program stopped.")



