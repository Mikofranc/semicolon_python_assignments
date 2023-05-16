def check_minimum_number(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    print(minimum)


numbers = [22, 3, 2, 99, 2, 1, 3]
check_minimum_number(numbers)
