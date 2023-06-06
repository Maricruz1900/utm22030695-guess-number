def guess_number():
    from random import randint

    ## determine the range of the number
    print("Choose the range of the random integer first the smallest number and then the largest.")

    # ask the user to input the starting number of the range
    number1 = int(input("Enter the first number: "))
    # ask the user to input the second number
    number2 = int(input("Enter the second number: "))
    random_number = randint(number1, number2)
    # set the starting points for the game to 100
    points = 100

    


