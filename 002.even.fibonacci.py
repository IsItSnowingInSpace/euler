#!/usr/bin/env python

fib1 = 1
fib2 = 2
loop = True
evenSum = 0

while ( loop == True ):
    if ( fib2 > 4000000):
        loop = False
        continue
    print "fib1 = " + str(fib1)
    print "fib2 = " + str(fib2) + "\n"
    if ( fib2 % 2 == 0 ): evenSum += fib2    
    x = fib1 + fib2
    fib1 = fib2
    fib2 = x

print "evenSum = " + str(evenSum)
