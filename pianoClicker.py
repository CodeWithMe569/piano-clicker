import pyautogui
import time
import keyboard
import win32api, win32con

# Tile 1 position: X:  378 Y:  457 RGB: (208, 180, 214)
# Tile 2 position: X:  453 Y:  491 RGB: (  0,   0,   0)
# Tile 3 position: X:  580 Y:  467 RGB: (187, 165, 214)
# Tile 4 position: X:  681 Y:  459 RGB: (182, 174, 225)

def click(x, y):
    """This function will set the cursor position according to the x and y value as parameters and perform a left click, wait for 0.01 seconds and then release the click"""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(378, 603)[0] == 0:
        click(378, 603)

    elif pyautogui.pixel(453, 603)[0] == 0:
        click(453, 603)

    elif pyautogui.pixel(580, 603)[0] == 0:
        click(580, 603)

    elif pyautogui.pixel(681, 603)[0] == 0:
        click(681, 603)


