from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
     q1 =  Question(text=i['text'],answer=i['answer'])
     question_bank.append(q1)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
     quiz.next_question()
score = quiz.score
question_number = quiz.question_number
print("You've completed the quiz")
print(f"Your final score was : {score}/{question_number}")
