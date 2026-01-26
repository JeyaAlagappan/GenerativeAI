import pyautogui
import time

# Give yourself a moment to focus away from other windows
print("The script will start in 3 seconds…")
time.sleep(3)

# 1) Open Start Menu
pyautogui.press('win')  # Press Windows key
time.sleep(1)

# 2) Type PowerPoint to search
pyautogui.write('PowerPoint', interval=0.1)
time.sleep(1)

# 3) Press Enter to launch the app
pyautogui.press('enter')

# Customize this delay depending on how long PowerPoint takes to open
time.sleep(5)

#Create a new blank presentation
pyautogui.press('enter')
time.sleep(2)

# Click on the title box to focus
pyautogui.click(553,259)  # Example coordinates — adjust as needed
time.sleep(0.5)

# Type the title
pyautogui.write("PyAutoGui Recording Demo", interval=0.1)  # types text slowly

# Save the file (Ctrl+S), type name, press Enter
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
#pyautogui.write("PyAutoGui_Dem", interval=0.05)
time.sleep(0.5)
pyautogui.press('enter')

time.sleep(0.5)

# Close PowerPoint
pyautogui.hotkey('alt', 'f4')

print("Done!")


