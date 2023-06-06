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

# create a loop that gives you 10 chances, and for each incorrect guess, deducts 10 points
    while True:
        print(f"The range of numbers is from {number1} to {number2}.")
        guess = int(input("Guess the number: "))
        
        # if you guess the number correctly, it prints the following message
        if guess == random_number:
            print("Congratulations! You guessed the random number!")
            break
        # if you don't guess correctly, deduct 10 points
        # you have a total of 10 chances
        else:
            print("Incorrect!")
            points -= 10
            if points == 0:
                # if you run out of points, it prints the following message
                print("You've lost all your points! Better luck next time!")
                break

            # after the first guess, it gives you a hint whether the number is higher or lower
            elif guess < random_number:
                # it indicates how many points you lose and how many points you have left
                print("The number is higher. You lose 10 points. Remaining points:", points)
            else:
                print("The number is lower. You lose 10 points. Remaining points:", points)

    # when you guess the number, it ends the game
    print("Game over.")

guess_number()






