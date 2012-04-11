#program to display root in readable form and not in decimals

import sys

def primes(n): 
	if n==2:
	    return [2]
	elif n<2:
	    return []
	
	s = range(3,n+1,2)
	mroot = n ** 0.5
	half = (n+1)/2 - 1
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:
			j = (m*m-3)/2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i+1
		m = 2*i+3
	return [2]+[x for x in s if x]



def factor(n):
    result = []
    prime = primes(n)
    #print 'Prime list ', prime
    for num in prime:
        #print num
        while n%num == 0:
            result.append(num)
            n = n/num
    return result

def root(n):
    factors = factor(n)
    answerout = 1
    answerin = 1
    pairs = {}
    for num in factors:
        if num in pairs:
            temp = pairs[num]
            pairs[num] = temp + 1
        else:
            pairs[num] = 1
    print pairs
    for nums in pairs:
        if pairs[nums]%2 == 0:
            answerout = answerout*(nums**(pairs[nums]/2))
        elif pairs[nums]>2:
            answerout = answerout*(nums**(pairs[nums]/2))
            answerin = answerin*nums
        else:
            answerin = answerin*nums
    print answerout, 'root', answerin
            

if len(sys.argv) == 1:
    print "Enter number"
else:   
    n = int(sys.argv[1])
    root(n)
    
