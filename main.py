import random

options = ["R", "P", "S"]


def rock_paper_scissors_game():
    status = True
    while status == True:
        cpu = random.choice(options)
        User_Input = input("Enter your choice...:")
        if User_Input == "R" or User_Input == "P" or User_Input == "S":
            print("Player({}) : CPU({})".format(User_Input, cpu))
            if cpu == User_Input:
                print("winner!!!")
                status = not(status)
        else:
            print("Player({}) : CPU({})".format(User_Input, cpu))
            print("Invalid choice...")

rock_paper_scissors_game()   