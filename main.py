#Title
print("Welcome to the Python Quiz!")

#Question 1



print("Question 1:")
print("What is the ouput of 2 + 2")
print(f"a) 3 ")
print(f"b) 4 ")
print(f"c) 5 ")
question_1 =input("")

if question_1 == "b":
    print(f"Your answer: {question_1}")
    print("Correct!")
    score1 = 1
elif question_1 == "a":
    print(f"Your answer: {question_1}")
    print(f"Incorrect!")
    score1 = 0
elif question_1 == "c":
    print(f"Your answer: {question_1}")
    print("Incorrect!")
    score1 = 0 
else:
    print("Invalid answer") 
    score1 = 0 


  

#Question 2

print("Question 2:")
print("Which of the following is a valid variable name in Python?")
print(f"a) 2variable ")
print(f"b) variable_name ")
print(f"c) variable-name ")
question_2 =input("")

if question_2 == "b":
    print(f"Your answer: {question_2}")
    print("Correct!")
    score2 = 1
elif question_2 == "a":
    print(f"Your answer: {question_2}")
    print(f"Incorrect!")
    score2 = 0
elif question_2 == "c":
    print(f"Your answer: {question_2}")
    print("Incorrect!")
    score2 = 0 
else:
    print("Invalid answer") 
    score2 = 0 

#Question 3

print("Question 3:")
print("What is the result of 'Hello' + 'World' in Python?")
print(f"a) HelloWorld ")
print(f"b) Hello World ")
print(f"c) Error ")
question_3 =input("")

if question_3 == "a":
    print(f"Your answer: {question_3}")
    print("Correct!")
    score3 = 1
elif question_3 == "b":
    print(f"Your answer: {question_3}")
    print(f"Incorrect!")
    score3 = 0
elif question_3 == "c":
    print(f"Your answer: {question_3}")
    print("Incorrect!")
    score3 = 0
else:
    print("Invalid answer") 
    score3 = 0

total_score = score1 + score2 + score3

print(f"You got {total_score}/3 correct!")
print("Thankyou for playing!")




 
