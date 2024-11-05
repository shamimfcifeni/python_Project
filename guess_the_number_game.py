import random
randomNumbers=random.randrange(1,200)
user_number=int(input("Enter the number:"))
if user_number>randomNumbers:
    print(randomNumbers)
    print("the num is too high")
elif user_number<randomNumbers:
    print(randomNumbers)
    print("the number is too low")
else:
    print(randomNumbers)
    print("you matched the num")