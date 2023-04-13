#QUIZ
print("Simple Math Quiz in Python")
user_name = str(input("Input User Name: "))
full_name = str(input("Input Full Name: "))
location = str(input("Input Location: "))
edu_level = str(input("Input Educational Level: "))

print ("Welcome", user_name)
ins = input("Are you ready to start? (yes/no): ")
score = 0
total_q =4
#q is the total no. of questions
if ins.lower() == "yes" : 
    print ("Let\'s Begin")
    
    ins = input("1. Which programming language is use for Data Science?")
    if ins.lower() == "python" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")

    ins = int(input("2. What is 2 * (30 // 6)"))
    if ins == "5" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")

    ins = int(input("3. Solve (20 % 6) * (15 % 4)"))
    if ins == "6" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")

    ins = input("4. Who is the lady that invented bluetooth, wifi and GPS?")
    if ins.lower() == "Hedy Lamarr" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")

    print("Thank you for Participating, You got", score, "questions correct.")
    mark = (score/total_q) * 100
    
    print("Mark: ", str(mark) + "%")
print("Goodbye")
