
import random
n = random.randrange(3, 5)
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


#Collage of photos
def collage_maker(image1, image2, name);
     i1 =np.array(image1)
     i2 =np.array(image2)
     collage =np.vstack([i1, i2])
     image = image.fromarray(collage)
     image.save(name)
