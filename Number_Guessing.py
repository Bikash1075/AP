import random
l = [*range(11)]
num= random.choice(l)
guess=int(input('Enter any number : '.title()))
while guess != num:
    if guess < num or guess > num:
        print ("it's incorrect")
        guess = int(input('Enter number again : '.title()))
    else:
        break
print('you guessed correct!'.title())
print(f'num is {num} and guess is {guess}')
    