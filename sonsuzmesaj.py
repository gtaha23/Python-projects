import pyautogui as yaz
import time

time.sleep(3)
def gonder():
    yaz.write("adana kebap")
    yaz.press("j")

for i in range(50):
    gonder()
    time.sleep(0)