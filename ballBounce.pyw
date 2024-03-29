import tkinter
from PIL import Image, ImageTk
import win32api, win32con, pywintypes

def update():
    #x, y = win32api.GetCursorPos()

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
    pos = "+250+250"
    label.master.geometry(pos)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "#000000")
    label.master.wm_attributes("-alpha", "1")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
    # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    # Load the image
    image = Image.open("ball.png")
    # Resize the image if necessary
    image = image.resize((r, r), Image.BILINEAR)
    # Convert the image for Tkinter
    ball_image = ImageTk.PhotoImage(image)

    # Use a Label to display the image
    ball_label = tkinter.Label(image=ball_image, borderwidth=0, highlightthickness=0, bg="#000000")
    ball_label.image = ball_image  # Keep a reference to avoid garbage collection
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
