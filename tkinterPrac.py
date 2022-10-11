from tkinter import *

window = Tk()

window.geometry("510x660")
bg = PhotoImage(file="LandingWithButton.png")

canvasStart = Canvas(window, width=510, height=660)
canvasStart.pack(fill="both", expand=True)

canvasStart.create_image(0, 0, image=bg, anchor="nw")

orderButton = Button(window, text="Order Here")
orderButton_canvas = canvasStart.create_window(
    205, 547, anchor="nw", window=orderButton)

window.mainloop()
