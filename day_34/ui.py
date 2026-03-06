from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN_COLOR = "#0ECA59"
RED_COLOR = "#FF474C"

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain

        TRUE_IMAGE = PhotoImage(file="images/true.png")
        FALSE_IMAGE = PhotoImage(file="images/false.png")
        
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=TRUE_IMAGE, highlightthickness=0,command=self.click_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=FALSE_IMAGE, highlightthickness=0,command=self.click_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question)
    
    def click_true(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("True"):
                self.give_feedback(True)
                self.score_label.config(text=f"Score: {self.quiz.score}")
            else:
                self.give_feedback(False)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz, Final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def click_false(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer("False"):
                self.give_feedback(True)
                self.score_label.config(text=f"Score: {self.quiz.score}")
            else:
                self.give_feedback(False)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz, Final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.reset_bg)
        
    def reset_bg(self):
        self.canvas.config(bg="white")
        self.get_next_question()