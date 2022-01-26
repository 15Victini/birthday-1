from datetime import date
import time

print("Now stealing your IP address. Do not resist.")
time.sleep(3)
print("I have stolen your IP address. Thank you for your compliance.")
print("You will now enter your birthday. Please enter 2 numeric digits for month and day, and 4 numeric digits for year.")
while True:
  try:
    m = int(input("Enter your birth month: "))
    if m>0 and m<13:
        break
    else:
        print("Please enter a valid month.")
        continue
  except ValueError:
      print("Please input integer only...")  
      continue

while True:
  try:
    d = int(input("Enter your birth day: "))
    if m == int("02"):
        if d>0 and d<30 and len(str(d)) == 2:
            break
        else:
            print("Please enter a valid day.")
            continue
    else:
        if d>0 and d<32:
            break
        else:
            print("Please enter a valid day.")
            continue
  except ValueError:
      print("Please input integer only...")  
      continue

while True:
  try:
    y = int(input("Enter your birth year: "))
    if len(str(y))==4:
        break
    else:
        print("Please enter a valid year. (Must be 4 characters)")
        continue
  except ValueError:
      print("Please input integer only...")  
      continue

print("You were born on:", m, d, y)

td = date.today()
print("This is today's date:", td)
print("There is less than a .27 percent chance that today is your birthday.")
print("so no happy birthday (probably)")
for i in range(5):
    print("ha")
    time.sleep(.75)
strtd = str(td)
a = int(strtd[0:4])-y
if int(strtd[5:7])>m:
    print("You are", a, "years old.")
elif int(strtd[5:7]) == m:
    if int(strtd[-2:]) >= d:
        print("You are", a, "years old.")
    else:
        print("You are", a-1, "years old.")
else:
    print("You are", a-1, "years old.")
