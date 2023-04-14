
def back(number):

    rev_number = 0

    while(number != 0):
        digit = number % 10
        rev_number = rev_number * 10 + digit
        number //= 10
    return rev_number


number = int(input("Give me a number: "))
print(back(number))