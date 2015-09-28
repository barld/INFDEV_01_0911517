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