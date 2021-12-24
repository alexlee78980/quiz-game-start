class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number].text
        correct = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {question} (True/False): ")
        self.check_answer(answer, correct)

    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            self.score += 1
            print("You got it right")
        else:
            print("that's wrong")
        print(f"The correct answer was: {correct}")
        print(f"Your current score is {self.score}/{self.question_number}")