# save dictionary to file
import pickle
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
    reg_file = username+"_details.txt"
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

    #quiz csv
    quiz_file_exists = os.path.isfile("quiz.csv")
    quiz_file = open("quiz.csv", "a", newline='')
    quiz_details = {'Topic' : topics[topic_selected], 'Difficulty' : difficulty[difficulty_selected], 'Username' : username}
    with quiz_file:
        quiz_file_header = ['Topic', 'Difficulty', 'Username']
        quiz_file_writer = csv.DictWriter(quiz_file, fieldnames=quiz_file_header)
        if not quiz_file_exists:
            quiz_file_writer.writeheader()
        quiz_file_writer.writerow(quiz_details)

    startQuiz(topics[topic_selected], difficulty[difficulty_selected])

#start selected quiz
def startQuiz(topic, difficulty):
    history_file = os.path.join(scriptpath, 'Quizes/history.csv')
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

    #if (topic == 'Computer Science'):
        #open comp sci quiz
    if (topic == 'History'):
        #open History quiz
        with open(history_file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                #skip the CSV header
                if skipHeader == 1:
                    skipHeader = 0
                    continue
                
                print("Question:")
                print(row[0])
                print("Here are your options")
                answer_list = [4, 3, 2, 1]
                for x in range(0, answers_shown):
                    #random_integer = random.randint(1,5)
                    shuffle(answer_list)
                    random_answers = answer_list[0]
                    del answer_list[0]
                    
                    answer_map = {x: row[random_answers]}

                    #checks for if answer
                    if(random_answers == 1):
                        isAnswerPresent = 1
                        answerID = x
                        
                    
                    print("Answer " + str(x) + " = " + row[random_answers])
                    
                print("The answer is " + str(answerID))
                answer_given = input("Enter your answer (Number only): ")
                if int(answer_given) == answerID:
                    score = score+1
                    print("Correct")
                else:
                    print("Sorry wrong answer")
        print(str(score))
                
        

########Start program##############
scriptpath = os.path.dirname(__file__)
initial = input("Enter 1 to Login or enter 2 to Register: ")


if initial == '1':
    username = login()
    if username is None:
        print("Login Failed")
    elif username is not None:
        quiz(username)
elif initial == '2':
    register()


