
class QuizBrain:
    """Contains three attributes: score, question_number, and questions. The questions attribute is initialized with quiz_brain object"""
    def __init__(self, question_pool):
        self.question_number = 0
        self.score = 0
        self.questions = question_pool

    def next_question(self):
            """Displays the next question to the user from the questions list using its index number.
            and invokes check_answer function to validate the answer entered by the user
            """
            next_question = self.questions[self.question_number]
            self.question_number += 1
            user_input = input(f"Question #{self.question_number}: {next_question.question}: 'q' to quit: ")
            self.check_answer(user_input, next_question.answer)

    def question_still_exists(self):
        """Returns a Boolean value indicating whether another question exists in the question pool"""
        return self.question_number < len(self.questions)

    def check_answer(self, user_input, actual_answer):
        """Validates the user's input, updates the score, and displays the total score.
        """
        if user_input == 'q':
            self.exit_game()
        elif user_input == actual_answer:
            self.score +=1
            print("You got it right!")
        else:
            print("That is wrong.")
            print(f"The actual answer is: {actual_answer}")
        print(f"Your score is {self.score}/{self.question_number}")

    @staticmethod
    def exit_game():
        quit()


