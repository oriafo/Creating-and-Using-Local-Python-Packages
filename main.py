import random

options = ["R", "P", "S"]


def rock_paper_scissors_game():
    cpu_Score = 0
    player_Score = 0 
    status = True
    while status == True:
        cpu = random.choice(options)
        User_Input = input("Enter your choice...:")
        if User_Input == "R" or User_Input == "P" or User_Input == "S":
            print("CPU({}) : Player({})".format(cpu, User_Input))
            if cpu == "R" and User_Input == "S":
                cpu_Score += 1
            elif cpu == "P" and User_Input == "R": 
                cpu_Score += 1
            elif cpu == "S" and User_Input == "P": 
                cpu_Score += 1
            elif User_Input == "R" and cpu == "S": 
                player_Score += 1
            elif User_Input == "P" and cpu == "R": 
                player_Score += 1
            elif User_Input == "S" and cpu == "P": 
                player_Score += 1
            elif cpu == User_Input: 
                print("Its a tie")
            else:
                print("nothing")
            status = not(status)
        else:
            ##print("CPU({}) : Player({})".format(cpu, User_Input))
            print("Invalid input.. Please input another value")
            #status = not(status)
        
    if cpu_Score > player_Score:
        print("winner is: CPU")
    elif cpu_Score < player_Score:
        print("winner is: Player")
    #else:
        #print("its a tie")

#the loop is not working

rock_paper_scissors_game()   