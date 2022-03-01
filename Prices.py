#def divider(x):
  #"-"*len(x)
  #return x
repeat = True
bal = 10

while True:
  repeat = True
  prices = {'apple':"2.65","banana":"1.69"}
  y = "Here are our items:"
  print(y+"\n"+"-"*len(y))
  for i in prices:
    print(i)
#print(divider(y))
  print()
#print(f"price of apple is {prices['apple']}")
  x = input("What item do you want?:\n")
  print()
  print(f"{x} costs ${prices[x]}")
  while repeat == True:
    answer = input("Pay? y/n:\n")
    if answer == "n":
      repeat = False
      print()
      print(f"Your balance: ${bal}")
      print()
      continue
    elif answer == "y":
      repeat = False
      bal -= float(prices[x])
      print()
      print(f"You have gained {x}.")
      print(f"Your balance: ${bal}")
      print()
      continue
