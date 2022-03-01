print("Welcome to seab's magic fortune teller :D")
print("Enter 4 numbers to check your fortune.")

x = "1st"

def question():
  g = int(input("Your "+x+" number:\n"))
  return g

n = 1
while n > 0:
  try:
    x = "1st"
    first = question()
    x = "2nd"
    second = question()
    x = "3rd"
    third = question()
    x = "4th"
    fourth = question()
    n -= 1
  except:
    print("plz enter a valid number!")

v = sum([first, second, third, fourth])

if len(str(v)) > 3:
  print("u have a meh future...\n+55 social credit.\n")
elif len(str(v)) > 2:
  print("bery gud future!\n+1000 social credit.\n")
else:
  print("terrible future :(\n-100000 social credit.\n)")
