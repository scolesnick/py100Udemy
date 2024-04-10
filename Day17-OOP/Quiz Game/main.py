from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []

for q_dict in question_data:
    questions.append(Question(q_dict['text'], q_dict['answer']))

# for q in questions:
#     print(f'Question:\n\t{q.text}\nAnswer:\n\t{q.answer}\n')

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.max_score}')