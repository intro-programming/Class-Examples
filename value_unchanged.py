# A formatted number does not change unless you put the format in a variable!

# Not Changed
number = 3.14389

print "Formatted: {0:.2f}".format(number)

print "Unformatted:", number

print "===================="

# Changed
number = 3.14389
print "Old Value:", number

# Not printing, but storing it back into variable number
number = "{0:.2f}".format(number)

print "New Value:", number

