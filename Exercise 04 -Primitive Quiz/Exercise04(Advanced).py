#Advanced Quiz for European Countries 
# Dictionary of countries and their capitals
European_countries = {
"Belgium": "Brussels",
"Austria": "Vienna",
"Portugal": "Lisbon",
"Switzerland": "Bern",
"Greece": "Athens",
"France": "Paris",
"Netherlands": "Amsterdam",
"Italy": "Rome",
"Germany": "Berlin",
"Spain": "Madrid"
}

# Ask the question
for country, capital in European_countries.items():
    answer = input(f"What is the capital of {country}? ")

    # Check if the answer is correct 
    if answer.lower() == capital.lower():
        print("The answer is correct!\n")
    else:
        print(f"The answer is wrong! It is {capital}.\n")