from game_data import data
import random
from art import logo, vs
from replit import clear

# Format account data into printable format.
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
 # Add art.
  print(logo)
  score = 0
  game_should_continue = True
# Generate a random account from the game data.
  account_a = random.choice(data)
  account_b = random.choice(data)

  while game_should_continue:
# Make game repeatable.
# Make B become the next A.
    account_a = account_b
    account_b = random.choice(data)
      
# Ensures that we are not comparing the same accounts. 
    while account_a == account_b:
      account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
 # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
      
# Clear screen between rounds.
    clear()
    print(logo)

# Check if user is correct.
# Get follower count.
    if is_correct:
      score += 1
# Feedback.
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
# Feedback.
      print(f"Sorry, that's wrong. Final score: {score}")

game()



