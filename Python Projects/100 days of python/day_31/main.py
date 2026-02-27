import random
from tkinter import *
import pandas

# ---------------------------- CONSTANTS -------------------------------
BACKGROUND_COLOR = "#B1DDC6"
CARD_FG = "./images/card_front.png"
CARD_BG = "./images/card_back.png"

# ---------------------------- DATA SETUP -------------------------------
data = pandas.read_csv("./data/french_words.csv")
words_dict = {row.English: row.French for (index, row) in data.iterrows()}
Correct = False
current_word = ""

# ---------------------------- UI SETUP (early init needed for PhotoImage) ------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file=CARD_FG)
card_back_img = PhotoImage(file=CARD_BG)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- FUNCTIONS -------------------------------
def random_word():
    global Correct, current_word
    Correct = False
    current_word = random.choice(list(words_dict.keys()))
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=words_dict[current_word], fill="black")
    window.after(3000, lambda: solve_word(current_word))

def mark_correct():
    global Correct
    Correct = True
    random_word()

def solve_word(word):
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word, fill="white")
    if Correct:
        data.drop(data[data.English == word].index, inplace=True)
        words_dict.pop(word, None)

# ---------------------------- BUTTONS -------------------------------
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=mark_correct)
right_button.grid(row=1, column=1)

random_word()
window.mainloop()