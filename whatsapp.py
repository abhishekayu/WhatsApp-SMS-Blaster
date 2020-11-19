import pyautogui
import webbrowser as w
import time

w.open("web.whatsapp.com")
time.sleep(30)

for i in range (1000000000):
	pyautogui.press("H")
	pyautogui.press("I")
	pyautogui.press("enter")
