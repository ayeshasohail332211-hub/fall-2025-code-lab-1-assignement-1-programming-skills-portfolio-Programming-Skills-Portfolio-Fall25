#Defining function to check if the number is even or odd
def even_or_odd(number):
    if number%2==0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
#Main function to get user input and display the result
def main():
    number= int(input("Enter the number: "))
    result= even_or_odd(number)
    print(result)

if __name__ == "__main__":
    main()