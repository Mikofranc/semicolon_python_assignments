import random

user_input = int(input(' Enter amount of time to trow a dice\n'))
print('=======================')
a =0
b = 0
c =0
d = 0
e = 0
f = 0

if user_input == 1:
    for number in range(user_input):
        no = random.randint(1, 6)
        if no == 1:
            a += 1
        if no == 2:
            b += 1
        if no == 3:
            c += 1
        if no == 4:
            d += 1
        if no == 5:
            e += 1
        if no == 6:
            f += 1

print(f'the no for 1 is {a}')
print(f'the no for 2 is {b}')
print(f'the no for 3 is {c}')
print(f'the no for 4 is {d}')
print(f'the no for 5 is {e}')
print(f'the no for 6 is {f}')
