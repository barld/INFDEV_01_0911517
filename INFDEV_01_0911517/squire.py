size = int(raw_input("wich size must the squire be: "))
filled = raw_input("must the squire be filled(f)? ").upper() == "F"

if(filled):
    print size*((size*"*")+"\n")
else:
    print size*"*"
    print ((size-2)*("*"+" "*(size-2)+"*\n"))[0:-1]
    print size*"*"
