# is PicoCTF up? Let's see?

import ctypes
import requests
import time
import platform

targetURL="https://2019game.picoctf.com"
status=0
ctypes.windll.user32.MessageBoxW(0, "PicoCTF", "Time to see when PicoCTF is up!", 1)
while(status != 200):
    req = requests.get(targetURL)
    status = req.status_code
    numOfMinutes=1
    time.sleep(60)

if platform.system() == "Linux":
    import tkinter
    from tkinter import messagebox
    display = tkinter.Tk()
    display.withdraw()

    messagebox.showwarning("2019 PICO CTF IS BACK UP", "GET HACKING!!")
elif platform.system() == "Windows":
    ctypes.windll.user32.MessageBoxW(0, "2019 PICO CTF IS BACK UP", "GET HACKING!!", 1)
