
def ex1a():
    fahrenheit = raw_input("input degrees fahrenheit you want to convert to celcius: ")
    fahrenheit = float(fahrenheit)
    print "C %0.2f" % ((fahrenheit-32.0)/1.8)

def ex1b():
    #http://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.htm
    C = float(raw_input("input C "))
    if(C < -273.15):
        print "temperature is lower than absolute zero there is no valid answer"
    else:
        print "K %0.2f" % (C + 273.15)

def ex1c():
    value = raw_input("give value you want to absolute ")
    value = int(value)
    if(value<0):
        value = value*-1
    print value

###################################################################################

def ex2a():
    print "welcome to rock paper scissors"
    def askUserInput():
        userInput = raw_input("choose rock(r), paper(p), scissors(s)").lower()
        if not(userInput == "r" or userInput == "p" or userInput == "s"):
            print "no valid input, try again!"
            return askUserInput()
        return userInput
    u1 = askUserInput()
    u2 = askUserInput()

    winner = ""
    if u1 == u2:
        winner = "You are both winner"
    elif u1 == "r":
        if u2 == "p":
            winner = "player 2 wins, paper cover rock"
        else:
            winner = "player 1 wins, rock cruches scissors"
    elif u1 == "p":
        if u2 == "r":
            winner = "player 1 wins, paper cover rock"
        else:
            winner = "player 2 wins, scissors cut paper"
    elif u1 == "s":
        if u2 == "r":
            winner = "player 2 wins, rock cruches scissors"
        else:
            winner = "player 1 wins, scissors cut paper"

    print winner


def ex2b():
    print "welcome to rock paper scissors lizard spock"
    def askUserInput():
        userInput = raw_input("choose rock(r), paper(p), scissors(s), lizard(l), spock(sp)").lower()
        if not(userInput == "r" or userInput == "p" or userInput == "s" or userInput == "l" or userInput == "sp"):
            print "no valid input, try again!"
            return askUserInput()
        return userInput
    u1 = askUserInput()
    u2 = askUserInput()

    winner = ""
    if u1 == u2:
        winner = "You are both winner"
    elif u1 == "r":
        if u2 == "p":
            winner = "player 2 wins, paper cover rock"
        elif u2 == "s":
            winner = "player 1 wins, rock cruches scissors"
        elif u2 == "l":
            winner = "player 1 wins, rock crushes lizard"
        elif u2 == "sp":
            winner = "player 2 wins, spock vaporizes rock"
    elif u1 == "p":
        if u2 == "r":
            winner = "player 1 wins, paper cover rock"
        elif u2 == "s":
            winner = "player 2 wins, scissors cut paper"
        elif u2 == "l":
            winner = "player 2 wins, lizard eats paper"
        elif u2 == "sp":
            winner = "player 1 wins, paper siproves spock"
    elif u1 == "s":
        if u2 == "r":
            winner = "player 2 wins, rock cruches scissors"
        elif u2 == "p":
            winner = "player 1 wins, scissors cut paper"
        elif u2 == "l":
            winner = "player 1 wins, scissors decapitates lizard"
        elif u2 == "sp":
            winner = "player 2 wins, spock smashes scissors"
    elif u1 == "l":
        if u2 == "r":
            winner = "player 2 wins, rock crushes lizard"
        elif u2 == "p":
            winner = "player 1 wins, lizard eats paper"
        elif u2 == "s":
            winner = "player 2 wins, scissors decapitates lizard"
        elif u2 == "sp":
            winner = "player 1 wins, lizard suopod spock"
    elif u2 == "sp":
        if u2 == "r":
            winner = "player 1 wins, spock vaporizes rock"
        elif u2 == "p":
            winner = "player 2 wins, paper siproves spock"
        elif u2 == "s":
            winner = "player 1 wins, spock smashes scissors"
        elif u2 == "l":
            winner = "player 2 wins, lizard suopod spock"

    print winner


ex2b()