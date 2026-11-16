from data import data
from question_model import Question
from quiz_brain import QuizBrain
from quiz_game_logo import logo

count = 0
question_pool = []
for text in data[0]['results']:
    """Question object created and appended to the list"""
    new_question = Question(text['question'], text['correct_answer'])
    question_pool.append(new_question)

if __name__ == '__main__':
    """The count variable is reset to 0 every time the user chooses to continue."""
    while count < 1:
        print(logo)
        quiz_pool = QuizBrain(question_pool)

        while quiz_pool.question_still_exists():
            quiz_pool.next_question()
        count += 1
        if count >= 1:
            user_input = input("Do you want to continue? (y/n): ")
            if user_input == 'y':
                count = 0
            else:
                quit()


