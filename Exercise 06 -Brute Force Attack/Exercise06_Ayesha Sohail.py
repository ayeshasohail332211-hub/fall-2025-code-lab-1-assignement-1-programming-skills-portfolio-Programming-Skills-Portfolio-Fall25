correct_password= "12345"
attempts_left= 5   #The user has only 5 attempts

#This will continue as long as the user still has attempts left
while attempts_left > 0 :
    attempt= input("Enter the password: ").strip()
    if attempt==correct_password:
        print("Access granted. You have entered the correct password!")
        break  #Correct password, loop stops
    else:
        attempts_left-=1
        if attempts_left>0:
            print(f"Incorrect Password. Try Again!({attempts_left} attempts remaining)")
        else:
            print("Too many failed attempts!")