class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
        self.max_score = 0

    def next_question(self):
        n = self.question_number
        question = self.question_list[n]
        self.question_number += 1
        ans = input(f'Q.{n+1}: {question.text} (True/False)?: ')
        self.check_answer(ans, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, ans):
        if user_ans.lower() == ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You suck")
        self.max_score += 1
        print(f'The correct answer was: {ans}')
        print(f'Your current score is: {self.score}/{self.max_score}.\n')