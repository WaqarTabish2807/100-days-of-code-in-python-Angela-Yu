from turtle import clear
from art import logo 
from art import vs
from game_data import data 
from turtle import clear
import random

print(logo)
score = 0
game_should_continue = True
acc_b = random.choice(data)

while game_should_continue: 

    acc_a = acc_b
    acc_b = random.choice(data)


    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A: {acc_a['name']}, a {acc_a['description']} from {acc_a['country']}")
    print(vs)
    print(f"Against B: {acc_b['name']}, a {acc_b['description']} from {acc_b['country']}")

    def check_answer(guess, a_count, b_count):

        if a_count > b_count:
            return guess == 'a'
        else:
            return guess == 'b'

    guess = input("Who has more followers? Type 'A' or 'B'").lower()

    a_count = acc_a['follower_count'] 
    b_count = acc_b['follower_count']
    is_correct = check_answer(guess, a_count, b_count)
    clear()
    print (logo)

    if is_correct:
        score += 1
        print(f"You're right! Correct score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry! That's wrong. Final score: {score}")
