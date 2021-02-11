from random import randrange


min = 1
max = 10
number_to_guess = randrange(min, max)

print(f'Guess number between {min} and {max}')

number_guessed = int(input())

while number_guessed is not number_to_guess:
  if number_guessed > number_to_guess:
    print('Number too high')
  else:
    print('Number too low')
  
  number_guessed = int(input())

print(f'Well done! The number was {number_guessed}')