#!/usr/bin/env python

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

sum = 0
next = 0

f = open('013.first-ten-sum.data', 'r')

for line in f:
    next = int(line.strip()[:11])
    sum += next

print str(sum)[:10]

f.close()


"""
for line in f:
    #if line.isdigit() == False: continue
    #print 'line = {0}'.format(line)

    next += int(line.strip()[:11])

    #print str(sum)
    #sum = int(str(sum)[:11])
    print str(sum)
"""
