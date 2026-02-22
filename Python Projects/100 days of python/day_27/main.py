import tkinter as tk

window = tk.Tk()
window.title("LBS To KG Converter")
window.minsize(width=250, height=50)
kg=0
lbs=0

lbs_input = tk.Entry(width=10)
lbs_input.grid(column=0, row=1,padx=10, pady=10)
lbs_label = tk.Label(text="LBS")
lbs_label.grid(column=1, row=1,padx=10, pady=10)

kg_result_label = tk.Label(text=f"{kg} KG")
kg_result_label.grid(column=3, row=1,padx=10, pady=10)

def exit_window(event=None):
    window.destroy()

def lbs_to_kg(event=None):
    global kg
    global lbs
    lbs = float(lbs_input.get())
    kg = round(lbs * 0.453592, 2)
    kg_result_label.config(text=f"{kg} KG")

convert_button = tk.Button(text="Convert", command=lbs_to_kg)
convert_button.grid(column=2, row=1,padx=10, pady=10)


window.bind("<Return>", lbs_to_kg)
window.bind("<Escape>", exit_window)        

window.mainloop()