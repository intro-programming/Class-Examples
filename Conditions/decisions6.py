# Using not keyword
color = raw_input("Enter your favorite color: ")

color = color.strip() # ignore for now

if not (color == "pink"):
    print "Cool color"
else:
    print "Whatever you like I guess :"