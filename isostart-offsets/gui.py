import pyautogui as pag
import time
import subprocess
import psutil
import pyperclip

PROCNAME = "ISOStartVC110.exe"
PROCPATH = "/home/denis/.wine/drive_c/Program Files (x86)/OBID/ID ISOStart 2017 - V9.09.10/"
pag.PAUSE = 2.5

def copy_clipboard():
    pag.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def open_isostart():
    subprocess.Popen(["wine", str(PROCPATH + PROCNAME)])
    time.sleep(4)

def print_screeninfo():
    screenWidth, screenHeight = pag.size()
    currentMouseX, currentMouseY = pag.position()
    
    print("Size: " + str(screenWidth) + "x" + str(screenHeight))
    print("CurrentMouse: " + str(currentMouseX) + "x" + str(currentMouseY))


def open_detect_interface():
    ## Detect interface
    pag.PAUSE = 0.5
    pag.hotkey('ctrl', 'd')
    
    ## Find text field
    pag.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    cb = copy_clipboard()
    print(cb)
    
    ## TCP/IP reader
    #pag.press(['tab', 'tab'])
    #pag.press(['space'])
    #time.sleep(10)
    #pag.hotkey('alt', 'd')
    pag.PAUSE = 2.5


def sleep(i):
    time.sleep(i)

def close_isostart():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

def main():
    open_isostart()
    print_screeninfo()
    open_detect_interface()
    time.sleep(10)
    
main()
## From pag documentation
#pag.moveTo(100, 150)
#pag.click()
#pag.moveRel(None, 10)  # move mouse 10 pixels down
#pag.doubleClick()
#pag.moveTo(500, 500, duration=2, tween=pag.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
#pag.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
#pag.press('esc')
#pag.keyDown('shift')
#pag.press(['left', 'left', 'left', 'left', 'left', 'left'])
#pag.keyUp('shift')
#pag.hotkey('ctrl', 'c')

