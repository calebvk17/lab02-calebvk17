# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).

def seconds_to_hms(total_seconds):

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"

def admission_price(age):

    price = 0.0

    if age < 5:
        price = 0.0
    if age >= 5 & age <= 12:
        price = 8.0
    if age >= 13 & age <= 64:
        price = 15.0
    if age >= 65:
        price = 10.0

    return price

def sum_multiples(limit):

    total = 0

    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i

    return total

def total_of_positives(numbers):

    total = 0

    for i in numbers:
        if i > 0:
            total = total + i

    return total

def main():

    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4


if __name__ == "__main__":
    main()