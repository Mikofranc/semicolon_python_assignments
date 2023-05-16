numbers = [7, 10, 27, 2, 92, 4]


def check_maximumNumber(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    print(maximum)


check_maximumNumber(numbers)