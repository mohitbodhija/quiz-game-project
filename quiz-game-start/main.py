from data import question_data
from question_model import question
from quiz_brain import Quizbrain

q_bank =[]

for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    new_question = question(q_text,q_ans)
    q_bank.append(new_question)

quiz= Quizbrain(q_bank)

while quiz.still_question_left:
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(q_bank)}")