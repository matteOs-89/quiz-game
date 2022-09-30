from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    question_t = ques["question"]
    question_a = ques["correct_answer"]
    new_question = Question(question_t, question_a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was  {quiz.score}/{quiz.question_number}")
