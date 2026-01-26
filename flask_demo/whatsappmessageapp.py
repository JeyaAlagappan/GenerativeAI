from flask import Flask, request, render_template_string
import pyautogui
import pyperclip
import time
import webbrowser
import threading

app = Flask(__name__)

# ------------------ WHATSAPP CHECK ------------------

def ensure_whatsapp_web_open():
    windows = pyautogui.getWindowsWithTitle("WhatsApp")

    if windows:
        windows[0].activate()
        print("✅ WhatsApp Web already open")
        time.sleep(3)
    else:
        print("🌐 Opening WhatsApp Web...")
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(15)  # wait for load / login


# ------------------ MESSAGE CONFIRMATION ------------------

def wait_for_message_sent(timeout=10):
    start = time.time()

    while time.time() - start < timeout:
        if pyautogui.locateOnScreen(
            "message_input_empty.png",
            confidence=0.8
        ):
            return True
        time.sleep(1)

    return False


# ------------------ SEND MESSAGE ------------------

def send_whatsapp_message(contact_name, message):
    ensure_whatsapp_web_open()

    # Click search box (adjust if needed)
    pyautogui.click(146, 204)
    time.sleep(1)

    pyautogui.write(contact_name)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)

    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    pyautogui.press("enter")

    # ✅ VERIFY REAL SEND
    if wait_for_message_sent():
        print("✅ Message successfully sent!")
        return

    print("⚠️ Message not confirmed. Retrying...")

    # Retry once
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")

    if wait_for_message_sent():
        print("✅ Message sent on retry!")
    else:
        print("❌ Message FAILED after retry")


# ------------------ HTML UI ------------------

HTML_FORM = """
<!doctype html>
<html>
<head>
  <title>WhatsApp Sender</title>
  <style>
    body { font-family: Arial; padding: 30px; }
    input, textarea { width: 100%; padding: 8px; margin: 8px 0; }
    button { padding: 10px 15px; font-size: 16px; }
  </style>
</head>
<body>
  <h2>Send WhatsApp Message</h2>
  <form method="POST" action="/send">
    <label>Contact Name:</label>
    <input type="text" name="contact" required>

    <label>Message:</label>
    <textarea name="message" rows="4" required></textarea>

    <button type="submit">Send Message</button>
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_FORM)

@app.route("/send", methods=["POST"])
def send_route():
    contact = request.form.get("contact")
    message = request.form.get("message")

    thread = threading.Thread(
        target=send_whatsapp_message,
        args=(contact, message)
    )
    thread.start()

    return "<h3>🚀 Message is being processed. Check WhatsApp Web.</h3>"


# ------------------ START APP ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
