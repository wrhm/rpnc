#polish_calc.py
'''
Implementation of a reverse Polish calculator.
'''

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
    vals = expr.split()
    if len(vals)==0: #print 'Invalid input.'
        return 'Need at least one value.'
    t = []
    while len(vals)>0:
        #print 'vals: %s, t: %s'%(vals,t)
        c = vals[0]
        if isNum(c):
            t = t + [float(c)]
        elif len(t)<2:
            return 'Not enough values on stack.' #return None
        else:
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
                return 'Unrecognized symbol: %s.'%c #return None
        vals = vals[1:]
    #print 'vals empty.'
    if len(t)==1:
        #return t[0]
        if t[0]-float(int(t[0]))==0.0: #truncate if whole number
            return int(t[0])
        else:
            return t[0]
    else:
        #return None
        return 'Not enough operators.'

if __name__ == "__main__":
    s = ''
    print '%s\n| RPN Calculator |\n%s\nValid operators: + - * / ^'%('='*18,'='*18)
    #help = 'Enter an expression, \'help\', or \'Exit\''
    #print help
    while True:
        #s = '3 5 + 7 / 4 * 2 -'
        s = raw_input('>> ')
        if 'exit' in string.lower(s):
            sys.exit()
        else:
            print '   = %s'%rpcVal(s)