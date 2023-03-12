class QuizBrain:

    def __init__(self,question_list):
        self.question_number=0
        self.question_list = question_list
        self.score=0
        #return self.question_list
    
    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q{self.question_number}: {question.text} (True/False) ? ")
        self.check_question(user_input,question.answer.lower().strip())

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            
    def check_question(self, user_input , question_answer):
        
        if user_input == question_answer:
            self.score+=1
            print(f"You are correct And Your current score is {self.score}/{len(self.question_list)} ")
        elif user_input != question_answer:
            print(f"Your answer is wrong And your final score is {self.score}/{len(self.question_list)} ")
        #elif self.user_input =="off":
             
        else:
            print(" Invalid Input ")  
        