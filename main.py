def fizzBuzz(upTo):
    number = 1
    while (number <= upTo):
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (number % 3 == 0):
            print("Fizz", end=' ')
        elif (number % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(str(number), end=' ')
        number = number + 1

fizzBuzz(35)