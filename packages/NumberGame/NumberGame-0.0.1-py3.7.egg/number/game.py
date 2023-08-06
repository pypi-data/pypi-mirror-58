import random
def number_game():
    while True:
        name=input("What is your name?")
        print("Hello " + name + "!")
        print("Would you like to play my game?")
        game=input("press g to play my game.")
        if game == "g":
            print("This is a guessing game. I am thinking of a number between 1 and 50. You have to guess that number.")
            ran=random.randint(1,50)
            print("You have five guesses")
            print()
            print("What is your first guess?")
            firnum=float(input())
            if int(firnum) == ran:
                print("Well done " + name + ". You have guessed my number!")
            else:
                if firnum < ran:
                    print("My number is higher.")
                if firnum > ran:
                    print("My number is lower.")
                print("What is your second guess?")
                secnum=float(input())
                if secnum == ran:
                    print("Well done " + name + ". You have guessed my number!")
                else:
                    if secnum < ran:
                        print("My number is higher.")
                    if secnum > ran:
                        print("My number is lower")
                    print("What is your third guess?")
                    trinum=float(input())
                    if trinum == ran:
                        print("Well done " + name + ". You have guessed my number!")
                    else:
                        if trinum < ran:
                            print("My number is higher.")
                        if trinum > ran:
                            print("My number is lower.")
                        print("What is your fourth guess?")
                        fornum=float(input())
                        if fornum == ran:
                            print("Well Done " + name + ". You have guessed my number!")
                        else:
                            if fornum < ran:
                                print("My number is higher.")
                            if fornum > ran:
                                print("My number is lower.")
                            print("What is your final guess?")
                            fifnum=float(input())
                            if fifnum == ran:
                                print("Well done " + name + ". You have guessed my number!")
                            else:
                                if fifnum < ran:
                                    print("My number is higher")
                                if fifnum > ran:
                                    print("My number is lower")
                                print("Sorry, " + name + ". You did not guess correctly. My number was,", ran)
                            a = input("Would you like to play again? press y for yes, and n for no")
                            if a == "y":
                                continue
                            if a == "n":
                                break
