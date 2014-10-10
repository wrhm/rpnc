#polish_calc.py
#Author: wrhm
#Implementation of a reverse Polish calculator.

import string, sys

#Evaluate a string via RPS rules,
#Returns None if invalid. (Assumes 
#single-digit values)
#ex: '54*3-' should yield 17.
'''
5 4 * 3 -
20 3 -
17
'''

def isNum(s):
    s = str(s)
    d = string.digits+'.'
    for c in s:
        if c not in d:
            return False
    return True

def rpcVal(expr):
    unary = ['fib']
    vals = expr.split()
    if len(vals)==0: #print 'Invalid input.'
        return 'Need at least one value.'
    t = []
    while len(vals)>0:
        #print 'vals: %s, t: %s'%(vals,t)
        c = vals[0]
        if isNum(c): #number (natural or decimal)
            t = t + [float(c)]
        elif c=='phi': #constant
            t = t+[rpcVal('5 1 2 / ^ 1 + 2 /')]
        elif len(t)==1: #unary operators
            if c=='fib':
                t = t[:-2]+[rpcVal('phi %s ^ 0 phi - 0 %s - ^ - 5 1 2 / ^ /'%(t[-1],t[-1]))]
            #if c== '!':
            #    l = 
            #    t = t[:-2]
        else: #binary operators
            if c=='+': #print 'Time to add.'
                t = t[:-2]+[t[-2]+t[-1]]
            elif c=='-': #print 'Time to subtract.'
                t = t[:-2]+[t[-2]-t[-1]]
            elif c=='*': #print 'Time to multiply.'
                t = t[:-2]+[t[-2]*t[-1]]
            elif c=='/': #print 'Time to divide.'
                if t[-1]==0:
                    return 'Error: division by zero.' #return None
                t = t[:-2]+[t[-2]/t[-1]]
            elif c=='^':
                t = t[:-2]+[t[-2]**t[-1]]
            else:
                if c in unary:
                    return '%s needs an argument.'%c
                #return 'Unrecognized symbol: %s.'%c #return None
        vals = vals[1:]
    #print 'vals empty.'
    if len(t)==1:
        #return t[0]
        if abs(t[0]-float(int(t[0])))<=1e-9: #truncate if (almost) whole number
            return int(t[0])
        else:
            return t[0]
    else:
        #return None
        return 'Not enough operators.'

if __name__ == "__main__":
    s = ''
    print '%s\n| RPN Calculator |\n%s'%('='*18,'='*18)
    print 'Valid operators: + - * / ^'
    print 'Valid values: naturals and decimals, and'
    print '   Constants: phi'
    #help = 'Enter an expression, \'help\', or \'Exit\''
    #print help
    while True:
        #s = '3 5 + 7 / 4 * 2 -'
        s = raw_input('>> ')
        if 'exit' in string.lower(s):
            sys.exit()
        else:
            print '   = %s'%rpcVal(s)
