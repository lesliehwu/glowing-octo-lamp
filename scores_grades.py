import random

def scores_grades():
    
    print("Scores and Grades")
    for x in range(10):
        random_num = random.randint(60,100)

        if(random_num >= 60 and random_num <= 69):
            my_grade = "D"
        elif(random_num >= 70 and random_num <= 79):
            my_grade = "C"
        elif(random_num >= 80 and random_num <= 89):
            my_grade = "B"
        elif(random_num >= 90 and random_num <=100):
            my_grade = "A"

        print("Score: " + str(random_num) + "; Your grade is " + my_grade)

print(scores_grades())

