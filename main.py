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
    reg_details = {'Name': name, 'Age': age, 'Year': year, 'Username': username, 'Password': password}
    login_details = {'Username' : username, 'Password' : password}


    #verify registration - if 3 characters of name in use, use more
   # verify_reg = pickle.load(open ("reg.txt", "rb"))
 #   if(username in verify_reg):
  #      for x in range(3, 10):
   #         if(name[:x] not in verify_reg):
    #            username = name[:x] + age
     #           reg_details = {username: password}
                #store into a file
      #          print("Your Username is: " + username)
       #         pickle.dump(reg_details, open ("reg.txt", "ab+"))
        #        break

    #store into a file
    print("Your Username is: " + username)
    #pickle.dump(login_details, open ("logins.txt", "ab+"))
    with login_file:
        login_file_header = ['Username', 'Password']
        login_file_writer = csv.DictWriter(login_file, fieldnames=login_file_header)
        if not login_file_exists:
            login_file_writer.writeheader()
        login_file_writer.writerow(login_details)    
    #pickle.dump(reg_details, open (reg_file, "ab+"))
                
register()
