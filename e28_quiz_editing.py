from random import *

#  Sets up the lists of questions
def setup(Questions, Answers) : 
    Questions.append("not ('testing' == 'testing' and 1 == 'Jan') ")
    Answers.append("True")
    Questions.append("'PAPER' == 'PAPER' and not ('testing' == 'testing' or 5 == 0) ")
    Answers.append("False")
    Questions.append("True and not ('testing' == 'testing' and 2 == 2) ")
    Answers.append("False")
    Questions.append("not (10 == 1 or 1000 == 1000) or 'true' == 'flase'")
    Answers.append("False")
    Questions.append("False and not ('testing' == 'resting' or 1 == 0)")
    Answers.append("False")
    Questions.append("'chair' == 'hair' or not (3 == 4 or 3 == 3)")
    Answers.append("False")
    Questions.append("1 == 1 and not ('quiz' == 'quiz' and 1 == 'Jan') ")
    Answers.append("True")


def Main() : 
    Questions = []  # list of all the  questions
    Answers = []    # list of all the answers 
    setup(Questions, Answers)
    score = 0
    numberAsked = 0
    while len(Questions) > 0 :
        qnNum = randint(0, len(Questions)-1)
        correct = askQuestion(Questions[qnNum], Answers[qnNum])
        numberAsked = numberAsked + 1
        if correct == "quit" :
            break
        elif correct :
            score=score+1
        del Questions[qnNum]
        del Answers[qnNum]

    print("Well done!  You got ", score, " questions right out of ", numberAsked)



#asks the user a question, and returns True or False depending on whether they answered correctly.
# If the user answered with 'q', then it should return "quit"
def askQuestion (question, correctAnswer):
    print(question)
    answer = input("True or False? (or quit)").lower()
    if answer == "quit" :
        return "quit"
    elif answer == correctAnswer.lower() :
        print("you got it! GJ!")
        return True
    else :
        print("No, that's wrong. The correct answer is ", correctAnswer)
        return False




Main()