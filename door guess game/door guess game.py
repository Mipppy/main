import things, time, random

correctdoor = random.randrange(1, 3)
good_thing = things.good_things[random.randrange(0, len(things.good_things))]
bad_thing = things.bad_things[random.randrange(0, len(things.bad_things))]

print("\n\nWelcome to the fun gameshow where you pick one of 3 doors, and whatever is \n behind it you are stuck with for the rest of your life!\nEnjoy!\n")
time.sleep(0.5)
try:
  door = int(input("Enter an door number: \n"))
except ValueError:
    print("Please input a door number only...")  
if door > 0 and door <= 3:
    if door == correctdoor:
       print(f'You won {good_thing}! \nCongrats!')
    else:
       print(f'You lost... but you still got {bad_thing}')
else:
   print("You should have entered a valid door number.") 