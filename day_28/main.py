import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ticks=" "
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def click_reset():
    global timer
    window.after_cancel(timer)
    global ticks, reps
    ticks = " "
    reps = 0
    track_label.config(text=ticks)
    top_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def click_start():
    global reps
    reps += 1
    if reps % 8 == 0:        
        count_down(LONG_BREAK_MIN*60)
        top_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        top_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        top_label.config(text="Work", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count//60:02d}:{count%60:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        click_start()
        global ticks, reps
        if reps % 2 == 0:
            ticks += "✔️"
            track_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


top_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
top_label.grid(column=1, row=0)

canvas = tk.Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = tk.Button(text="Start", highlightthickness=0, command=click_start)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(text="Reset", highlightthickness=0, command=click_reset)
reset_btn.grid(column=2, row=2)


track_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15),text=ticks)
track_label.grid(column=1, row=3)



window.mainloop()
