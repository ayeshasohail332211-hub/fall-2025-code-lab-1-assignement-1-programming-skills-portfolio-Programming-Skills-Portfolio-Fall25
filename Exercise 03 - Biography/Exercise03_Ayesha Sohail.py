#Using 'input()' function to ask users for their information
Name= input("Enter you name: ")
Hometown= input("Enter your hometown: ")
#Using 'int' data type to make sure the age is a number and not a string
Age= int (input("Enter your age: "))

#Storing the information in a dictionary 
personal_info= { 
    "name": Name,
    "hometown": Hometown,
    "age": Age, 
}

#Printing the personal information in a single line
print(personal_info["name"], personal_info["hometown"], personal_info["age"], sep="\n")
