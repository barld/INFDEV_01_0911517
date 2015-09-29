# will always return True
def trueFunction():
    print "truefunction"
    return True

# will always return false
def falseFunction():
    print "falseFunction"
    return False


"""
first with binairy operator than with logical and operator

With an binary operator it will always evaluate the whole expresion
With the logical and operator it wil not always evaluate the whole expresion. 
e.g. if the first expresion there is no reason to check the second value

"""
print falseFunction() & trueFunction()
print "--------------------------------"
print falseFunction() and trueFunction()

print "#########################"

def isNull():
    return True

def doSomething():
    raise Exception("is null")

print not isNull() and doSomething()

print "--------------------"

try:
    print not isNull() & doSomething()
except Exception as e:
    print "on no an exception:", e.message


print "--- string length ------"

s = "hallo"

print len(s) > 9 and s[9] == "a"

print len(s) > 9 & s[9] == "a"
