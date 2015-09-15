print "welkom to triangle.py"

size =0

while True:
    try:
        size = int(raw_input("enter a number: "))
    except ValueError:
        print "come on give me a real number!"
        continue
    break

for i in range(size, 1, -1):
    if i == size:
        print str(i*"*")+ str(" "*(size-(i+1)))
    else:
        print str(i*"*")+ str(" "*(size-(i+1)))+str("*")

print size*"*" 