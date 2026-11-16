from Data import data
from QuestionModel import Question
from QuizBrain import QuizBrain
from QuizGameLogo import logo

class QuizTest:

    def __init__(self, new_data):
        self.data = new_data
        self.question_pool = []

    def play_quiz(self):
        print(logo)
        self.get_data(self.data)
        quiz_pool = QuizBrain(self.question_pool)
        QuizTest.get_next_question(quiz_pool)

        user_input = input("Do you want to continue? (y/n): ")
        if user_input == 'y':
            print(logo)
            self.play_quiz()
        else:
            quit()

    def get_data(self, new_data):
        for text in new_data[0]['results']:
            """Question object created and appended to the list"""
            new_question = Question(text['question'], text['correct_answer'])
            self.question_pool.append(new_question)

    @staticmethod
    def get_next_question(quiz_pool):
        while quiz_pool.question_still_exists():
            quiz_pool.next_question()

if __name__ == '__main__':
    quiz = QuizTest(data)
    quiz.play_quiz()


