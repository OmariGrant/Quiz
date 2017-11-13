#CSV file
import csv
import os.path
#random number
import random
from random import shuffle

#registration function
def register():
    #get input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    year = input("Enter your year group: ")
    password = input("Enter your password: ")
    username = name[:3] + age
    #set up CSV file
    login_file_exists = os.path.isfile("login.csv")
    login_file = open("login.csv", "a", newline='')
    
    #put into dictionary
    login_details = {'Username' : username, 'Password' : password, 'Name': name, 'Age': age, 'Year': year}

    #store into a file
    print("Your Username is: " + username)
    with login_file:
        login_file_header = ['Username', 'Password', 'Name', 'Age', 'Year']
        login_file_writer = csv.DictWriter(login_file, fieldnames=login_file_header)
        if not login_file_exists:
            login_file_writer.writeheader()
        login_file_writer.writerow(login_details)

#login function
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    login_file = os.path.join(scriptpath, 'login.csv')

    with open(login_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if username == row[0] and password == row[1]:
                print("Logged in as " + username)
                username_ver = username
                return username_ver
    
#run quiz setup
def quiz(username):
    #set input
    print("quiz by " + username)
    topics = {'1': 'Computer Science', '2': 'History'}
    difficulty = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
    #get topic and difficulty
    print("Please select a topic")
    for key, value in topics.items():
        print("Enter number " + key + " for ", value)
    topic_selected = input("Which topic would you like? (Enter number only): ")

    print("Please select difficulty")
    for key, value in difficulty.items():
        print("Enter number " + key + " for ", value)
    difficulty_selected = input("Which difficulty would you like? (Enter number only): ")

    ##start quiz and get score
    score = startQuiz(topics[topic_selected], difficulty[difficulty_selected])
    grades_all = {100: "A", 80: "B", 60: "C", 40: "D", 20: "E"}
    percentage = score * 20
    grade = grades_all[percentage]
    print("You Scored: " + str(score) + " out of 5 which is " + str(percentage) + "% and a grade " + str(grade))
    

    #quiz csv
    quiz_file_exists = os.path.isfile("quiz.csv")
    quiz_file = open("quiz.csv", "a", newline='')
    quiz_details = {'Topic' : topics[topic_selected], 'Difficulty' : difficulty[difficulty_selected], 'Username' : username, 'Score': score, 'Percentage': percentage, 'Grade': grade}
    with quiz_file:
        quiz_file_header = ['Topic', 'Difficulty', 'Username', 'Score', 'Percentage', 'Grade']
        quiz_file_writer = csv.DictWriter(quiz_file, fieldnames=quiz_file_header)
        if not quiz_file_exists:
            quiz_file_writer.writeheader()
        quiz_file_writer.writerow(quiz_details)



#start selected quiz
def startQuiz(topic, difficulty):
    
    isAnswerPresent = 0
    score = 0
    answerID = -1
    skipHeader = 1
   
    
    if (difficulty == 'Easy'):
        answers_shown = 2
    elif (difficulty == 'Medium'):
        answers_shown = 3
    elif (difficulty == 'Hard'):
        answers_shown = 4

    if (topic == 'Computer Science'):
        #open comp sci quiz
        filename = os.path.join(scriptpath, 'Quizes/compsci.csv')
    ######History Quiz########
    if (topic == 'History'):
        #open History quiz
        filename = os.path.join(scriptpath, 'Quizes/history.csv')
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            #skip the CSV header
            if skipHeader == 1:
                skipHeader = 0
                continue
            
            print("Question:")
            print(row[0])
            print("Here are your options")
            if difficulty == "Hard":
                answer_list = [4, 3, 2, 1]
            elif difficulty == "Medium":
                answer_list = [4, 3, 1]
            elif difficulty == "Easy":
                answer_list = [3, 1]
            for x in range(0, answers_shown):
                
                shuffle(answer_list)
                random_answers = answer_list[0]
                del answer_list[0]
                
                answer_map = {x: row[random_answers]}

                #checks for if answer
                if(random_answers == 1):
                    isAnswerPresent = 1
                    answerID = x

                print("Answer " + str(x) + " = " + row[random_answers])
                
            answer_given = input("Enter your answer (Number only): ")
            if int(answer_given) == answerID:
                score = score+1
                print("Correct")
            else:
                print("Sorry wrong answer")
    return score
                
###report by username
def reportByUser():
    quiz_file = os.path.join(scriptpath, 'quiz.csv')
    username = input("Enter a confirmed username: ")
    with open('quiz.csv', newline='') as f:
        reader = csv.reader(f)
        print('"Topic", ', '"Difficulty", ', '"Username", ', '"Score", ', '"Percentage", ', '"Grade"')
        for row in reader:
            if username == row[2]:
                print(row)

##report by topic and difficulty
def reportByTopic():
    quiz_file = os.path.join(scriptpath, 'quiz.csv')
    avg_score = 0
    total_score = 0
    high_score = 0
    high_scorer = ""
    counter = 0
    
    topic = input("Enter 1 for Computer Science or 2 for History: ")
    if topic == "1":
        topic = "Computer Science"
    elif topic == "2":
        topic = "History"
    difficulty = input("Enter 1 Easy or 2 for Medium or 3 for Hard: ")
    if difficulty == "1":
        difficulty = "Easy"
    elif difficulty == "2":
        difficulty = "Medium"
    elif difficulty == "3":
        difficulty = "Hard"
        
    with open('quiz.csv', newline='') as f:
        reader = csv.reader(f)
        print('"Topic", ', '"Difficulty", ', '"Username", ', '"Score", ', '"Percentage", ', '"Grade", ')
        for row in reader:
            if topic == row[0] and difficulty == row[1]:
                print(row)
                counter=counter+1
                total_score = total_score + int(row[3])
                if high_score <= int(row[3]):
                    high_scorer = row[2]
                    high_score = int(row[3])
                   

    ##work out average and high score 
    avg_score = total_score / counter
    print("The average score of this quiz and difficulty is " + str(avg_score))
    print('The high score was by '  + high_scorer + ' with a score of ' + str(high_score))
    
                
        
########Start program##############
scriptpath = os.path.dirname(__file__)
initial = input("Enter 1 to Login or enter 2 to Register or 3 for Fergus Username Tool or 4 Topic Tool: ")


if initial == '1':
    username = login()
    if username is None:
        print("Login Failed")
    elif username is not None:
        quiz(username)
elif initial == '2':
    register()
elif initial == '3':
    reportByUser()
elif initial == '4':
    reportByTopic()

