import random
from replit import clear

def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):    
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(uscore, cscore):
  if cscore > 21 and uscore > 21:
    return "You lose miserably. You went over 21."
  if uscore == cscore:
    return "It is a draw. Better luck next time."
  elif cscore == 0:
    return "You lose. The Computer has a Blackjack :("
  elif uscore == 0:
    return "Congratulations. Blackjack, you win!"
  elif uscore > 21:
    return "Oh man. You went over 21. You lost."
  elif cscore > 21:
    return 'Congrats. You have won!!! Computer went over 21.'
  elif uscore > cscore:
    return 'You win!'
  else: 
    return "You lose!"

def play_game():

  user = []
  comp = []
  is_game_over = False
  for _ in range(2):
    user.append(deal_cards())
    comp.append(deal_cards())

  while not is_game_over:
    uscore = calculate_score(user)
    cscore = calculate_score(comp)
    print(f"Your cards: {user}, current score: {uscore}")
    print(f"Computer's first card: {comp[0]}")

    if (uscore == 0 or cscore == 0 or uscore>21):
      is_game_over = True
    else: 
      choice = input("Type 'y' to get another card, type 'n'to pass: ").lower()
      if (choice == "y"):
        user.append(deal_cards())
      else: 
        is_game_over = True
        print("Game Over")

  while cscore!=0 and cscore<17:
    comp.append(deal_cards())
    cscore = calculate_score(comp)

  print(f"Your final cards are: {user}, final score: {uscore}")
  print(f"Computer final cards are: {comp}, final score: {cscore}")
  print(compare(uscore,cscore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

    





