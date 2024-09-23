import random

name = input("Enter your name: ")
print(f'hello {name} i have a number between 1 and 100, you have say me what is it, have 8 chances')

my_number = random.randint(1, 100)
chances = 0
number = 101
while chances < 8:
    number = int(input('Enter your number: '))
    if number == my_number:
        print(f'congratulations you win on {chances + 1} chance')
        break
    elif number > 100 or number < 1:
        print('your number is out of range')
    elif number > my_number:
        print('your number is bigger than mine')
    elif number < my_number:
        print('your number is smaller than mine')
    chances += 1
    print(f'you have {8-chances} chances')