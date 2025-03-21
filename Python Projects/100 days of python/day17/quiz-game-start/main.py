from question_model import Question
from data import question_data
from os import system
from quiz_brain import QuizBrain
import random

system("cls")

question_bank=[]

for i in range(len(question_data)):
    question=Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question)


q_b=QuizBrain(question_bank)
while q_b.still_has_questions():
    q_b.next_question()
    print("\n"*2)

print(f"You have completed the quiz with the final score: {q_b.score}/{len(question_bank)}")