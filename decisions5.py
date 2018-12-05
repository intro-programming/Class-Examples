# Using or keyword
color = raw_input("Enter your favorite color: ")

color = color.strip() # ignore for now

if color == "red" or color == "blue":
    print "I like that color too!"
else:
    print "What a boring color..."