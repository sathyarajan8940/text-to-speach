import tkinter as tk
from tkinter import *
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init(driverName='sapi5')   # Use 'espeak' on Linux, 'nsss' on Mac
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speaknow():
    text = textv.get().strip()
    if text:
        engine.say(text)
        engine.runAndWait()   # Do NOT call engine.stop() here

root = Tk()
textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=("Arial", 12), bd=2)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(obj, text="Text:", font=("Arial", 11))
lbl.pack(side=tk.LEFT, padx=5)

entry = Entry(obj, textvariable=textv, font=("Arial", 12), width=25, bd=5)
entry.pack(side=tk.LEFT, padx=10)

btn = Button(obj, text="Speak", font=("Arial", 11, "bold"), 
             bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False, False)
root.mainloop()
