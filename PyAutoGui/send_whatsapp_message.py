import pyautogui
import pyperclip
import time
import webbrowser

# Open WhatsApp Web in default browser
webbrowser.open("https://web.whatsapp.com")

# Wait for WhatsApp Web to load
time.sleep(15)

print("WhatsApp Web opened successfully!")


# Contact name (exactly as in WhatsApp)
contact_name = "Hubby"

# Message to send
message = "Hello 👋 This message was sent using PyAutoGUI 🚀"

# Click on search box (adjust coordinates if needed)
pyautogui.click(146,204)
time.sleep(1)

# Type contact name
pyautogui.write(contact_name)
time.sleep(2)

# Press Enter to open chat
pyautogui.press('enter')
time.sleep(1)

# Copy message to clipboard (emoji-safe)
pyperclip.copy(message)

# Paste message
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Send message
pyautogui.press('enter')

print("Message sent successfully ✅")
