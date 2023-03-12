import webbrowser
import sys
import pyautogui as pe
from time import sleep

query = ' '.join(sys.argv[1:])
url = f"https://chat.openai.com/chat"
webbrowser.open(url)
sleep(2)
pe.typewrite(query)
sleep(1)
pe.press('enter')