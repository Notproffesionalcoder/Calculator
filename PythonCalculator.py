# This code was originally made by user mentos1386 @ http://code.runnable.com/UzMVYY9BxuQgTLiK/basic-python-calculator-for-simple-and-beginner
#
#My first program in Python. Im still learning this programing language.

running = True 

while running:
    print "1 = Addition"
    print "2 = Subtraction"
    print "3 = Multiplication"
    print "4 = Division"
    print "5 = Exit program"
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print "Addition"
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first + second
        print " "
        print first," + ",second," = ",result
        print " "
    elif cmd == 2:
        print "Subtraction"
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first - second
        print first," - ",second," = ",result
    elif cmd == 3:
        print "Multiplication"
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first * second
        print first," x ",second," = ",result
    elif cmd == 4:
        print "Division"
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first / second
        print first," : ",second," = ",result
    elif cmd == 5:
        print "Quit!"
        running = False
