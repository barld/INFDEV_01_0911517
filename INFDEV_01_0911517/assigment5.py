# https://github.com/hogeschool/INFDEV01-1/blob/master/assignments/DEV%20I%20Assignment%20V.pdf
def ex1():
    input = raw_input("put in something to reverse:\t")
    output = ""
    index = 0
    while index < len(input):
        output = input[index] + output
        index+=1
    print output

def ex2():
    #not a real count does always count + 1
    def count(m, input):
        amount = 1
        for char in input:
            if m(char):
                amount += 1
        return amount

    def isSpecialChar(input):
        return ord(input) < 48 or 57 < ord(input) < 65 or 90 < ord(input) < 97 or ord(input) > 122


    input = raw_input("give password:\t")
    points = len(input) * count(str.isupper, input) * count(str.islower, input) * count(str.isdigit, input) * count(isSpecialChar, input)

    if points < 1000:
        print "your password is weak"
    elif points < 2500:
        print "your password is medium"
    else:
        print "your password is strong"


def ex3():
    sInput = raw_input("put in a string: ")
    iInput = int(raw_input("input an int: "))

    nString = ""

    for char in sInput:
        offset = 97 if str.islower(char) else 65
        num = (ord(char) - offset + iInput + 26) % 26
        nString += chr(num+offset)

    print rtw