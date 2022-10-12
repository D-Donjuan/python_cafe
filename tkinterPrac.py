from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Python Cafe")
# window.geometry("0x0")
bg = PhotoImage(file="LandingWithButton.png")

canvasStart = Canvas(window, width=510, height=660)
canvasStart.pack(fill="both", expand=True)


def openNewWindow():
    newWindow = Toplevel(window)
    newWindow.geometry("200x200")


def close():
    win.quit()


canvasStart.create_image(0, 0, image=bg, anchor="nw")

orderButton = Button(window, text="Order Here",
                     bg='tan', command=openNewWindow)
orderButton_canvas = canvasStart.create_window(
    205, 547, anchor="nw", window=orderButton)

window.mainloop()
