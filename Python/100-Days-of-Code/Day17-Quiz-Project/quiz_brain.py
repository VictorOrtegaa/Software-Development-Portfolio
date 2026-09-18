class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def still_has_question(self):
        return self.question_number < len(self.question_list)



    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_a= input(f"Q.{self.question_number}: {current_q.question} is it (True?) or (False?): ")
        while user_a.lower() != "true" and user_a.lower() != "false":
            print("Please type True or False.")
            user_a = input("Try again: ")
        self.check_answer(user_a, current_q.answer)

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            self.score += 1
            print("Correct buddy!")
        else:
            print("Incorrect mate!")
        print(f"The correct answer was: {correct_a}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

