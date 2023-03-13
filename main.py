import webbrowser
import sys
import pyautogui as pe
from time import sleep

query = ' '.join(sys.argv[1:])
url = f"https://chat.openai.com/chat"
print('Starting up your Browser...')
webbrowser.open(url)
sleep(4)
pe.typewrite(query)
sleep(1)
pe.press('enter')