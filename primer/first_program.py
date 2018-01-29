def isEqual(num1, num2):
    if num1<num2:
        print(str(num1) + ' is too small!')
        return False
    if num1>num2:
        print(str(num1) + ' is too big!')
        return False
    if num1 == num2:
        print('Bingo!')
        return True

from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False

while bingo == False:
    answer = input()
    if answer:
        isEqual(int(answer), num)
