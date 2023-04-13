#QUIZ
print("Simple Math Quiz in Python")
#user_name = str(input("Input User Name: "))
#full_name = str(input("Input Full Name: "))
#location = str(input("Input Location: "))
#edu_level = str(input("Input Educational Level: "))

#print ("Welcome", user_name)
#ins = input("Are you ready to start? (yes/no): ")
score = 0
#if ins.lower() == "yes" : 
    #print ("Let\'s Begin")
    
def pythonCheck():
    inst = input("1. Which programming language is use for Data Science?")   
    if inst.lower() == "python" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")
            
    return score 

def numberCheck(score):
    ins = int(input("2. What is 2 * (30 // 6)"))
    if ins == 5:
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")
        
    return score
 
def stringCheck(score) : 
    ans = int(input("3. Solve (20 % 6) * (15 % 4)"))
    if ans == 6:
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")

    return score

def wordCheck(score) :
    anst = input("4. Who is the lady that invented bluetooth, wifi and GPS?")  
    if anst.lower() == "hedy lamarr" :
        score =+ 1
        print("Correct!")
    else:
        print("Incorrect")
        
    return score
    
final_Score = numberCheck(pythonCheck()) ,wordCheck(stringCheck(score))
print("Your Final Score Is",  final_Score)

    
#print("Mark: ", str(mark) + "%")
#print("Goodbye")
