from question_model import question


class Quizbrain:
    def __init__(self,q_list) -> None:
        self.question_number =0
        self.question_list = q_list
        self.score =0

    def is_correct(self,user_ans,corr_ans):
        if user_ans.lower()==corr_ans.lower():
            print("Your answer is correct")
            self.score +=1
        else:
            print("Thats Incorrect")
        print(f"Correct answer is {corr_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number +=1
        ans = input(f"Q. {self.question_number} :{curr_question.text} (True/False): ")
        self.is_correct(ans,curr_question.answer)
    
    def still_question_left(self):
        if self.question_number<=len(self.next_question) :
            return True
        else:
            return False
    
    

