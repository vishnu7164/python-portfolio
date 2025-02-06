#(1). Guess a number

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count<guess_limit:
    guess = int(input('enter a number: '))
    guess_count+=1
    if guess == secret_number:
        print('Congrats you guessed it right')
        break
    elif guess_count==2:
        print('This is your last chance')
else:
    print('Failed!, You guessed it wrong')

#(2). To make the program more dynamic random.randint()  method is used


import random 
secret_number = random.randint(0,9)
guess_count = 0
guess_limit = 3

while guess_count<guess_limit:
    guess = int(input('Guess a number between 0 and 9: '))
    guess_count+=1
    if guess == secret_number:
        print('Congrats you guessed it right')
        break
    elif guess_count==2:
        print('This is your last chance')
else:
    print('Failed!, You guessed it wrong')
    print(f'Computer has guessed: {secret_number}')