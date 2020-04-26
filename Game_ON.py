import random


def welcome():
    """This is the welcome page of the game, let us begin"""
    for i in range(0, 20):
        print("*\t", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*", end="")
    print()
    print("*", end="")
    for i in range(0, 9):
        print("\t", end="")
    print("WELCOME", end="")
    for i in range(0, 9):
        print("\t", end="")
    print("*", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*", end="")
    print()
    for i in range(1, 20):
        print("*\t", end="")
    print("*", end="")
    print()
    print()
    input("Please enter any key to start: ")


def mainmenu():
    print("\n1.Rock,Paper and Scissors\n2.Cows and Bulls\n3.Exit")
    ans1 = int(input("Please enter your choice: "))
    if ans1 == 1:
        RPSmenu()
    elif ans1 == 2:
        CBmenu()
    elif ans1 == 3:
        exit()
    else:
        print("\n***** Invalid choice,please enter a number from 1-3 *****\n")
        mainmenu()


def RPSmenu():
    print("\n1.Play\n2.Rules\n3.Return to main menu")
    ans2 = int(input("Please enter your choice: "))
    if ans2 == 1:
        RPSplay()
    elif ans2 == 2:
        RPSrules()
    elif ans2 == 3:
        mainmenu()
    else:
        print("\n***** Invalid choice,please enter a number from 1-3 *****\n")
        RPSmenu()


def RPSplay():
    print("WELCOME TO ROCK,PAPER AND SCISSORS")
    print("You will be competing against the computer.The player that scores 5 points first wins the game..."
          "\nFor Rock,enter 1\n"
          "For Paper, enter 2\n"
          "For Scissors, enter 3\n"
          "Enter 0 to exit the game")
    user = 0
    comp = 0
    count = 0
    ch = ['Null', 'Rock', 'Paper', 'Scissors']
    while (user < 5 and comp < 5 and count < 25):
        count += 1
        u_inp = int(input("\nEnter your choice here: "))

        if u_inp == 0:
            print("Thank You")
            return
        c_inp = random.choice([1, 2, 3])
        if u_inp == 1 and c_inp == 2:
            comp += 1
        elif u_inp == 1 and c_inp == 3:
            user += 1
        elif u_inp == 2 and c_inp == 1:
            user += 1
        elif u_inp == 2 and c_inp == 3:
            comp += 1
        elif u_inp == 3 and c_inp == 1:
            comp += 1
        elif u_inp == 3 and c_inp == 2:
            user += 1
        print("You:", ch[u_inp])
        print("Computer:", ch[c_inp])
        print(f"Your score: {user}\tComputer score: {comp}")
    if (user > comp):
        print("\n\n ***** Congratulations, you win!! *****")
    elif (comp > user):
        print("\n\n***** Oops, sorry you lost.Better luck next time *****")
    else:
        print("\n\n***** Draw *****")
    mainmenu()


def RPSrules():
    print(
        """\nA player who decides to play rock will beat another player who has chosen scissors\n("rock crushes scissors" or sometimes "blunts scissors"),\nbut will lose to one who has played paper ("paper covers rock");\na play of paper will lose to a play of scissors ("scissors cuts paper").\nIf both players choose the same shape, the game is tied and is usually immediately replayed\nto break the tie.\n""")
    ch = int(input("\nPlease enter 0 to return to the game: "))
    if ch == 0:
        RPSmenu()
    else:
        print("Please enter a valid choice")
        RPSrules()


welcome()
print("\n")
mainmenu()

# def CBmenu():
#     print("\n1.Play\n2.Rules\n3.Return to main menu")
#     ans3 = int(input("Please enter your choice: "))
#     if ans3 == 1:
#         CBplay()
#     elif ans3 == 2:
#         CBrules()
#     elif ans3 == 3:
#         mainmenu()
#     else:
#         print("\n***** Invalid choice,please enter a number from 1-3 *****\n")
#         CBmenu()
#
#
# def CBplay():
#     pass
#
#
# def CBrules():
#     pass
#
#
# welcome()
# print("\n")
# mainmenu()
