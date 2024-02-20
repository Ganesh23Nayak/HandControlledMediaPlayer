import tkinter as tk
from dataCollection import datacollection
import tkinter.font as font

window=tk.Tk()
window.title("Welcome")
window.geometry("400x400")

frame1 = tk.Frame(window)

label= tk.Label(window, text="WELCOME",fg="black")
label.pack()


btn_font = font.Font(size=15)
btn1 = tk.Button(frame1,fg="red", text="add data",command=datacollection, height=5, width=10)
btn1['font'] = btn_font
btn1.grid(row=0, column=0, padx=(5,5), pady=(10,10))

btn2 = tk.Button(frame1,fg="orange", text="train",command=" ", height=5, width=10)
btn2['font'] = btn_font
btn2.grid(row=0, column=1, padx=(5,5), pady=(10,10))

btn3 = tk.Button(frame1,fg="green", text="run",command=" ", height=5, width=10)
btn3['font'] = btn_font
btn3.grid(row=0, column=2, padx=(5,5), pady=(10,10))

frame1.pack()
window.mainloop()