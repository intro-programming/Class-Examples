# Testing for more than one condition
age = float(raw_input("Enter your age: "))
grade = int(raw_input("Enter your grade: "))

if age >= 8:
    if grade >= 3:
        print "You can play this game."
else:
    print "Sorry, you can not play this game."