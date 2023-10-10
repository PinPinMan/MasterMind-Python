# 6diff colors with 4Holes P(Win) = 6^4
import random
colours = ["🔴","🔵","🟠","🟡","🟢","🟣"]
start = """
                       _oo0oo_                      
                      o8888888o
                      88" . "88
                     (|  -_-  |)
                     0\   =   /0 
                   ___/` --- '\___

            Welcome to PinPin's MasterMind
             ( ? )   ( ? )   ( ? )   ( ? )
=======================================================
(1)🔴Red
(2)🔵Blue
(3)🟠Orange
(4)🟡Yellow
(5)🟢Green 
(6)🟣Purple 
======================================================="""
won = """=======================================================
             ({})   ({})   ({})   ({})   
                Congraluation 🎊🎉✨
                    Attemps: ({})          
                   ***THANK YOU*** \n"""
forfit = """=======================================================
             ({})   ({})   ({})   ({})  
                    Attemps: ({})          
                   ***THANK YOU*** """

def mastermind():
    ans = [colours[random.randrange(0,len(colours))] for i in range(4)]
    print(ans)
    attempts = 0
    round_history = []
    print(start)
    
    while True:
        attempts += 1
        correctInput = False
        while not correctInput:
            guess = input("\nInput 4 numbers (1-6)\n\t- ")
            if len(guess) == 4:
                for i in guess:
                    if i in ["1","2","3","4","5","6"]:
                        continue
                    else:
                        print("Only Numbers (1-6)")
                        break
                else:
                    correctInput = True
            else:
                print("Only 4 numbers")


        guess_colour = []
        checker = []
        for index, val in enumerate(guess):
            colour = colours[int(val)-1]
            guess_colour += [colour]
            if ans[index] == colour:
                checker += "⚫"
            elif colour in ans:
                checker += "⚪"
            else:
                checker += "🟤"


        display_guess = "\t(?)   (?)   (?)   (?)"
        display_checker = "\t(?)   (?)   (?)   (?)"
        for index in range(4):
            display_guess = display_guess.replace("?",guess_colour[index],1)
            display_checker = display_checker.replace("?",checker[index],1)
        print(display_guess,display_checker,sep="\n")


        round_history.append(["".join(guess_colour),"".join(checker)])


        if not ("⚪" in checker or "🟤" in checker):
            print(won.format(ans[0],ans[1],ans[2],ans[3],attempts))
            break
        
        correctRound = False
        while not correctRound:
            next_round = input("\nForfit (F) / Continue (C)? ")
            if next_round in ["f","c","F","C"]:
                correctRound = True
            else:
                print("Only F or C")

        if next_round.lower() == "f":
            print(forfit.format(ans[0],ans[1],ans[2],ans[3],attempts))
            return [round_history,attempts,"".join(ans),"f"]


    print(attempts,round_history,"".join(ans))
    return [round_history,attempts,"".join(ans)]


def display_summary():
    option_display = "\nSummary (Select An Option / Exit (E) / Clear (C))"
    global history
    if history == {}:
        print(option_display,"="*len(option_display),"\tNo History 😈\n", sep="\n")
        return 0

    while True:
        print(option_display)
        print("="*len(option_display))
        for round_index in history:
            round = history[round_index]
            if round[-1] == "f":
                print("\t({}) Game{} ({}) Attemps: ({}) *Forfit".format(round_index,round_index,round[2],round[1]))
            else:
                print("\t({}) Game{} ({}) Attemps: ({})".format(round_index,round_index,round[2],round[1]))
        
        correctOption = False
        while not correctOption:
            option = input("\t>> ")
            if option in ["s","e","c","S","E","C"] or option in [str(i) for i in option]:
                correctOption = True
            else:
                print("Only (S,C,E) or (1-{})".format(len(history)))


        if option.lower() == "c":
            history = {}
            print("\nHistory Cleared!\n")
            break
        elif option.lower() == "e":
            print("\nBye!\n")
            break
        elif int(option) in history:
            print("\n({0}) Game{0}".format(option),"=========================",sep="\n")

            for rounds in history[int(option)][0]:
                print("({}) ({})".format(rounds[0],rounds[1]))
            if round[-1] == "f":
                print("========(Forfited)=======")
            else:
                print("=========================")

history = {}
round = 0
while True:
    action = input("Wanna Play A Game? (Y) / Show Summary (S) / Exit (E): ")
    if action.lower() == "y":
        round += 1
        history[round] = mastermind()
    elif action.lower() == "s":
        display_summary()
    elif action.lower() == "e":
        print("\nThank You!")
        break
    else:
        print("Only S or Y or E\n")