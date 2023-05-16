weight = input('enter weight: \n')
unit = input("Enter 'L' for kg ===Enter 'k' for Lbs\n")

if unit.upper() == 'L':
    total = int(weight) * 5
    print(f'your are {total} kilo')
elif unit.upper() == 'K':
    total = int(weight) / 5
    print(f'you are {total} libos')
else:
    input('enter right digit')
