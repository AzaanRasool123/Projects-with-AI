import random

# List of countries
countries = ["France", "Spain", "Italy", "Germany", "China", "Japan", "USA", "Brazil", "Australia", "India"]

def country_guessing_game():
    # Choose a random country from the list
    country_to_guess = random.choice(countries)

    # Initialize the number of attempts
    attempts = 0

    print("Welcome to the country guessing game!")
    print("I'm thinking of a country. Try to guess it!")

    while True:
        # Ask the user for their guess
        user_guess = input("Enter your guess: ")

        # Check if the user's guess is correct
        if user_guess.lower() == country_to_guess.lower():
            print(f"Congratulations! You guessed the country in {attempts + 1} attempts.")
            break
        else:
            print("Sorry, that's not correct. Try again!")
            attempts += 1

if __name__ == "__main__":
    country_guessing_game()