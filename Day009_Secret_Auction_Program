import os
from turtle import clear
os.system('clear') 
  
bidamt = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${bid_amount}")


while not bidding_finished:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  bidamt["name"] = bid
  new = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if new == "no":
    bidding_finished = True
    find_highest_bidder(bidamt)
  elif new == "yes":
    clear()
   

