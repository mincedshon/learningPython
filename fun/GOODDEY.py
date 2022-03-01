print("Enter your friends name!")
names = []
b = 1
while True:
  x = input(f"Friend no.{b}:\n")
  if x == "stop":
    break
  names.append(x)
  b += 1
  print("Enter 'stop' if u have no more frens")

while True:
  g = input("Enter Y for a greeting:\n")
  if g == "Y":
    break

for i in names:
  print("GUD DEY "+i+"!!!!!!!")
