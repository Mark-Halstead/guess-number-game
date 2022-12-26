import random

# Generate a random number between 1 and 10
target = random.randint(1, 10)

# Initialize the number of tries
tries = 0

# Print a message to the user
print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

# Loop until the user has made 3 guesses
while tries < 3:
  # Get a guess from the user
  guess = int(input("Enter your guess: "))
  
  # Increment the number of tries
  tries += 1
  
  # Check if the guess is correct
  if guess == target:
    # If the guess is correct, print a message and exit the loop
    print("Congratulations! You guessed the correct number.")
    break
  else:
    # If the guess is incorrect, print a message and continue the loop
    print("Sorry, that's not the correct number. Try again.")

# If the user has made 3 guesses, print a message
if tries == 3:
  print("Sorry, you've run out of chances. The correct number was {}.".format(target))
