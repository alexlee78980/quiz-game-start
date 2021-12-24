from question_model import Question
from data import question_data
import quiz_brain

question_bank = []
for question in question_data:
    question_bank.append(Question(question.get("text"), question.get("answer")))

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
