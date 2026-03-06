
class QuizBrain:

    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
        

    def next_question(self):
        q=self.question_list[self.question_number]
        ans=input(f"Q.{self.question_number+1}: {q.text}(True\False)? ").lower()
        self.question_number+=1
        self.check_answer(ans,q.answer)
    
    def check_answer(self,u_ans,c_ans):
        if u_ans==c_ans.lower():
            print("Correct!")
            self.score+=1
        else:
            print("Wrong!")

        print(f"Correct answer was: {c_ans}")
        print(f"Current Score: {self.score}/{self.question_number}")