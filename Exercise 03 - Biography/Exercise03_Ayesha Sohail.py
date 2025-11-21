#Using 'input()' function to ask users for their information
name= input("Enter you name: ")
hometown= input("Enter your hometown: ")

#Checking the age input
while True:
    user_age= input("Enter your age: ")
    if user_age.isdigit():  
        age= int(user_age)
        break
    else:
        print("Enter a valid number for the age")


#Storing the information in a dictionary 
personal_info= { 
    "name": name,
    "hometown": hometown,
    "age": age 
}

#Printing the personal information in a single line
print(personal_info["name"], personal_info["hometown"], personal_info["age"], sep="\n")
