
import random
n = random.randrange(5000, 10000)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n :
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again"))
    else:
    break
print("you guessed it right")


#Average(Mean)
list1 = [1509,6776,6565,2343,2524,2524,2656,25256]
mean = sum(list1)/len(list1)
print (mean)



