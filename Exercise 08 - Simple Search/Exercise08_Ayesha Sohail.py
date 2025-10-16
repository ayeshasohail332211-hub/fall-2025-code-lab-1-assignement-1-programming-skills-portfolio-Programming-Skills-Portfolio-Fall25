list_of_names= ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"] #List of names
name= input("Enter the name you want to search: ") #Ask the user for the name to search

#Check if the name exists in the list
if name in list_of_names:
    print (f"{name} was found in the list.")
else:
    print (f"{name} was not found in the list.")