import tkinter as tk

window = tk.Tk()
window.title("python dev gui")
window.minsize(width=500, height=300)
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(align="center")

while True:
    window.mainloop()