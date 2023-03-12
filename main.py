from question_class import questions
from question_data import question_data
import random
import sys
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=questions(question_text,question_answer.lower().strip())
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions:
 quiz.next_question()
 







#print(question_bank[0].answer)
# game="on"
# random.shuffle(question_bank)
# score=0
# while game =="on":
#     max= len(question_bank)
#     #i=random.randint(0,max)
#     #print(i)
#     for i in range(0,max):
#      if score==max-1:
#         print("Thanks for playing this game ")
#         sys.exit()
#      if i==max:
#         sys.exit()
#      print(f"Q{i+1}: {question_bank[i].text}")
#      print(question_bank[i].answer)
     
#      user_answer=input("Is it True Or False -- ").lower().strip()
#      if user_answer=="true" or user_answer== "false":
#        if user_answer==question_bank[i].answer:
#         print("You are correct ")
#         score+=1
#         print(f"Your current score is {score}")
#        elif user_answer!=question_bank[i].answer:
#         print("Sorry You are wrong ")
#         print(f"Your Final score is {score}")
#         sys.exit()
#      elif user_answer=="off":
#           game=="off"   
#           sys.exit()   
       
#      else:
#         print("Invalid input. Please check your response again ")
    