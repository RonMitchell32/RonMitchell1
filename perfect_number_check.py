def is_perfect_number(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        return True
    else:
        return False

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is a perfect number
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
