import pyautogui
import time
"""
#Mouse Operationsclear
pyautogui.click(100,100)
time.sleep(2)
pyautogui.rightClick(100,100)
time.sleep(2)
pyautogui.rightClick(1296,425)

#keyboard operations
time.sleep(4)
pyautogui.write("clear")
pyautogui.press("enter")
pyautogui.hotkey('ctrl','a')
"""
#image
location=pyautogui.locateOnScreen(r'C:\Users\ssure\OneDrive\Desktop\Jeyu\copilot.jpg',confidence=0.08)
print(location)
time.sleep(3)
pyautogui.click(pyautogui.center(location))
