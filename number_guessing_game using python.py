import random
n = random.randrange(1,10)
guess = int(input("Enter a any number between 1 to 10 : "))
while n != guess:
    if guess < n :
        print("your guess number is too low ")
        guess = int(input("Enter a number again : "))
    elif guess > n :
        print("your guess number is too high ")
        guess = int(input("Enter a number again : "))
    else:
        break
print("you guessed it right! ")