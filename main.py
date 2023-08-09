from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


bank = []
for question in question_data:
    texts = question['question']
    answers = question['correct_answer']
    pairs = Question(texts, answers)
    bank.append(pairs)


quiz = QuizBrain(bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

