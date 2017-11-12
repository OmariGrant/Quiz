# save dictionary to file
import pickle
#CSV file
import csv
import os.path


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
                
register()
