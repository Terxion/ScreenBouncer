import tkinter
from PIL import Image, ImageTk
import win32api, win32con, pywintypes

def update():

    global x,y,sx,sy,r
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    
    if(x<=0 or x+r>=w):
        sx*=-1
    if(y<=0 or y+r>=h):
            sy*=-1

    x += sx
    y += sy
    
    pos = "+" + str(round(x)) + "+" + str(round(y))
    label.master.geometry(pos)
    label.after(10, update)  # run itself again after 10 ms

def main():

    label.master.overrideredirect(True)
    label.master.geometry("+1+1")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "#000000")
    label.master.wm_attributes("-alpha", "1")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    image = Image.open("ball.png")
    image = image.resize((r, r), Image.BILINEAR)
    ball_image = ImageTk.PhotoImage(image)

    ball_label = tkinter.Label(image=ball_image, borderwidth=0, highlightthickness=0, bg="#000000")
    ball_label.image = ball_image
    ball_label.pack()

    update()
    label.mainloop()

if __name__ == "__main__":

    sx = 10
    sy = 10
    x = 1
    y = 1
    r = 100
    
    label = tkinter.Label()
    main()
