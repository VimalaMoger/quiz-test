from data import data
from QuestionModel import Question
from QuizBrain import QuizBrain
from quiz_game_logo import logo

def get_data(data_source):
    questions_pool = []
    for text in data_source[0]['results']:
        """Question object created and returns the list"""
        new_question = Question(text['question'], text['correct_answer'])
        questions_pool.append(new_question)
    return questions_pool

def get_next_question(quiz_pool):
    while quiz_pool.question_still_exists():
        quiz_pool.next_question()

def play_quiz(data_source):
    print(logo)
    questions_pool = get_data(data_source)
    question = QuizBrain(questions_pool)
    get_next_question(question)

    user_input = input("Do you want to continue? (y/n): ")
    if user_input == 'y':
        print(logo)
        play_quiz(data_source)
    else:
        quit()

if __name__ == '__main__':
   play_quiz(data)


