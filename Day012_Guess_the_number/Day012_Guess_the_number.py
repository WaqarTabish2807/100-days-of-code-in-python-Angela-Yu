import random

print("Welcome to the number guessing game")
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")


choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if choice == 'easy': 
  n=10
else: 
  n=5

while (n>0):
  print(f"You have {n} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too high")
    if n>1:
      print("Guess again")
  elif guess < number: 
    print("Too low")
    if n>1:
      print("Guess again")
  else: 
    print(f"You got it. The answer was {number}")
    n=0

  n-=1
  if n==0:
    print("You've ran out of guesses, you lose.")

