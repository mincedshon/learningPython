#Randomizer will pick a value from 1-100
#print out 1-100
#player selects a value
#1-100 will change depending on value
import random
answer = random.randint(2,99)
small = 1
big = 100
x = 1
names = []
selName = True
y = 0
players = 0
b = 0

print("Welcome to the game. Players will take turns entering a number and the range will get smaller. The goal is to not hit the number!")
players = int(input("Please enter number of players:\n"))

while selName == True:
  if x <= players:
    userName = input(f"Player {x}'s name:\n")
    names.append(userName)
    x += 1
  else:
    selName = False

while True:
  y = names[b]

  print(f"\nPlayer {y}'s turn.")
  try:
    guess = int(input(f"{small}-{big}\nYour answer: "))
    bad = f"{guess} is not a valid number"

    if guess == small:
      print(bad)
      continue

    if guess == big:
      print(bad)
      continue

    if guess == answer:
      break

    if guess > answer:
      if guess < big:
        big = guess
      else:
        print(bad)
        continue

    if guess < answer:
      if guess > small:
        small = guess
      else:
        print(bad)
        continue

    if big - small == 2:
      if b == int(players)-1:
        b = -1
      b += 1
      y = names[b]
      break

    if b == int(players)-1:
      b = -1
    b += 1

  except:
    print("Please enter a legit number")


print(f"The bomb is {answer}")
print(f"You lose, Player {y}!!!")
