import random
x = random.randint(0, 10)
print(x) # verification
print("Guess the number between 1 and 10!")
y = int(input("Your guess: "))

while (y != x):
    if(y > x):
        y = int(input("Lower! "))
    elif(y < x):
        y = int(input("Higher! "))
print("Congrats! The number was " + str(y))
        
