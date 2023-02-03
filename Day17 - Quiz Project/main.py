#! /usr/bin/env python3

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question'] 
    question_answer = question['correct_answer']
    quiz_data = Question(question_text,question_answer)
    question_bank.append(quiz_data)

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    for item in question_bank:
        quizBrain.next_question()
        
print(f"You've completed the quiz.")  
print(f"Your final score was: {quizBrain.score}/{len(quizBrain.question_list)}")



        