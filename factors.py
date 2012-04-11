import sys
import math

def factors(n):
    fact = [1,n]
    check = 2
    rootn = n**0.5
    while check<rootn:
        if n%check == 0:
            fact.append(check)
            fact.append(n/check)
        check += 1
    if rootn == check:
        fact.append(check)
        fact.sort()
    return fact
        
n = int(sys.argv[1])
print factors(n)
