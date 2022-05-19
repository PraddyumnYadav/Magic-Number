import random

magicNumber = random.randint(1, 10)
userInput = ""


def take_input(i):
    print(f"Guess and Enter The The Magic Number from 1 to 10 You Have {i} Chance:")
    global userInput
    try:
        userInput = int(input("-:> "))
    except:
        print("Please Enter a Larger Number")
        userInput = int(input("-:> "))


take_input(5)

for i in range(1, 5):
    if userInput == magicNumber:
        print("You Win")
        break
    elif userInput >= magicNumber:
        print("You Entered too Larger Number Please Enter a Smaller Number .")
        take_input(5 - i)
    elif userInput <= magicNumber:
        print("You Entered too Smaller Number Please Enter a Larger Number .")
        take_input(5 - i)
    print()
else:
    print("You Loss")

print("Thanks for Playing This Game .")