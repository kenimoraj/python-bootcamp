from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank = []

for q in question_data["results"]:
    question = Question(q["question"],q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

ui = QuizInterface(quiz)
print(f"You've completed the quiz! Your score was {quiz.score}/{len(quiz.question_list)}")