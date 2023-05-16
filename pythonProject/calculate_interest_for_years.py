principal_amount = int(input('ENTER PRINCIPAL:         '))
no_of_year = int(input('ENTER NO OF YEAR:      '))
print()


def calculate_interest_in_years(amount: int, no_of_years: int):
    rate = 0.05
    for year in range(1, no_of_years + 1):
        roi = amount * rate
        future_value = amount + roi
        amount = future_value
        print(f'year {year} return on invest is 50% your principal  is now  N{amount: ,.2f}\n')


calculate_interest_in_years(principal_amount, no_of_year)
