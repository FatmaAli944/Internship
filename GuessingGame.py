import random


secret_number = random.randint(1, 10)

print("welcome to guessing game")
print("you have chosen anumber between 1 and 10 <<you only have tree attempts to guess>>")


for attempt in range(1, 4):
   
    guess = int(input(f"attempts number {attempt}:enter your guess : "))

   
    if guess == secret_number:
        print(f"you won ! the number is : {secret_number} ")
        break 
    elif guess < secret_number:
        print("the number is  greater than the number you selected ")
    else:
        print("the number is  smaller than the number you selected ")


else:
    print(f"your attempts have ended !! the seccret number is : {secret_number}")