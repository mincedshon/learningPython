import random
symbol = ["7","X","@","¥","?"]
rate = [200,50,40,30,20]
social_credits = 50
win7=winX=winAt=winYen=winNani=0
lose = 0
n = 0
x = 0
win_value = 500

def execute(a,c):
  global social_credits
  x = f"+{rate[a]}"
  social_credits += rate[a]
  print(c)
  print(f"{x} social credits")
  print(f"Your social credits: {social_credits}")

def lose_count():
  global lose
  print("Better luck next time!")
  lose += 1

while True:
  if social_credits < 3:
    break
  if n == 0:
    print("Welcome to social credit miner 2000!")
    print("-"*10)
    print("You are currently trapped in a casino with 50 social credits.\n")
    print("To leave, you have to acquire 500 social credits.")
    print("-"*10)
    start = input("Press any key to start:\n")
  x = "-3"
  social_credits -= 3
  #say_bal = f"Your social credits: {social_credits}"
  print("-"*10)
  print(f"{x} social credits")
  print(f"Your social credits: {social_credits}")
  print("-"*10)
  n += 1
  print(str.upper("<s.c.m 2000>"))
  ran1 = random.randint(0,4)
  ran2 = random.randint(0,4)
  ran3 = random.randint(0,4)
#print("{ran1} {ran2} {ran3}".format("7","&","$")
  print("["+symbol[ran1]+"]"+"["+symbol[ran2]+"]"+"["+symbol[ran3]+"]")

  if ran1 == ran2:
    if ran2 == ran3:
      if ran3 == 0:
        execute(0,"Jackpot!!")
        win7 += 1
      elif ran3 == 1:
        execute(1,"Awesome!")
        winX += 1
      elif ran3 == 2:
        execute(2,"Great!")
        winAt += 1
      elif ran3 == 3:
        execute(3,"Not bad!")
        winYen += 1
      elif ran3 == 4:
        execute(4,"Getting somewhere!")
        winNani += 1

    else:
      lose_count()
      print(f"Your social credits: {social_credits}")
  if ran1 != ran2:
    lose_count()
    print(f"Your social credits: {social_credits}")

  if social_credits > win_value:
    break
  print("-"*10)
  reset = input("Press any key to try again with 3 social credits:\n")
  if reset == "end":
    break
  continue

if social_credits < 3:
  print("You lose!!")
else:
  print("Congratulations!! You got out!!")
print(f"\nYou have played {n} rounds.\nJackpots: {win7}\nLoses: {lose}")
