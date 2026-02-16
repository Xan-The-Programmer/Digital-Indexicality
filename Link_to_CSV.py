import pyautogui
x,y = 1200,440

pyautogui.moveTo(x,y)
pyautogui.click(x,y)
pyautogui.keyDown('shift')
pyautogui.keyDown('right')
