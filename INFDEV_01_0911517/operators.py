def trueFunction():
    print "truefunction"
    return True

def falseFunction():
    print "falseFunction"
    return False

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
