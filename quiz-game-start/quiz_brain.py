import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        question.question_text = html.unescape(f"Q{self.question_number}: {question.question_text}")
        # ans = input(f"Q.{self.question_number}: {question.question} (True/False) ")
        # self.check_answer(question, ans)
        return question

    def check_answer(self, question,answer):
        if answer == question.answer:
            feedback = "Correct!"
            self.score += 1
            return True
        else:
            feedback = "Wrong!"
            return False

        # print(f"{feedback} The correct answer was {question.answer}.\nYour score is {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
