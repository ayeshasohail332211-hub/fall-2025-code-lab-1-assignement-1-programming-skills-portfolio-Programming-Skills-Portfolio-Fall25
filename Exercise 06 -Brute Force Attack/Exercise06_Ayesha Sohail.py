correct_password= "12345"
#The code will run until the user enters the correct password
while True:
    attempt= input("Enter the password: ").strip()
    if attempt==correct_password:
        print("Access granted. You have entered the correct password!")
        break
    else:
        print("Invalid password. Try Again!")