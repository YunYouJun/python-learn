from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False

while bingo == False:
    answer = eval(input())

    if answer < num:
        print(str(answer) + ' is too small!')

    if answer > num:
        print(str(answer) + ' is too big!')

    if answer == num:
        print('Bingo!')
        bingo = True
        