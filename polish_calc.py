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

def rpcVal(expr,trace):
    unary = ['fib']
    binary = ['+','-','*','/','^']
    tokens = expr.split()
    if len(tokens)==0:
        return 'Need at least one token.'
    values = []
    while len(tokens)>0:
        if trace: print 'tokens: %s, values: %s'%(tokens,values)
        c = tokens[0]
        if isNum(c): #number (natural or decimal)
            values.append(float(c))
        elif c=='phi': #constant
            values = values+[rpcVal('5 1 2 / ^ 1 + 2 /',trace)]
        elif len(values)==0: return 'Need at least one value.'
        elif len(values)<=1: #unary operators
            if c=='fib': # overflows if argument > 1474
                values = values[:-2]+[rpcVal('phi %s ^ 0 phi - 0 %s - ^ - 5 1 2 / ^ /'%(values[-1],values[-1]),trace)]
            else:
                if c in binary:
                    return 'Not enough values.'
                else:
                    return 'Unrecognized symbol: %s.'%c
        else:#elif len(values)==2: #binary operators
            if c=='+': #print 'Time to add.'
                values = values[:-2]+[values[-2]+values[-1]]
            elif c=='-': #print 'Time to subtract.'
                values = values[:-2]+[values[-2]-values[-1]]
            elif c=='*': #print 'Time to multiply.'
                values = values[:-2]+[values[-2]*values[-1]]
            elif c=='/': #print 'Time to divide.'
                if values[-1]==0:
                    return 'Error: division by zero.' #return None
                values = values[:-2]+[values[-2]/values[-1]]
            elif c=='^':
                values = values[:-2]+[values[-2]**values[-1]]
            #else:
            #    if c in unary:
            #        return '%s needs an argument.'%c
        tokens = tokens[1:]
    #print 'tokens empty.'
    if trace: print 'tokens: %s, values: %s'%(tokens,values)
    if len(values)==1:
        if abs(values[0]-float(int(values[0])))<=1e-9: #truncate if (almost) whole number
            return int(values[0])
        else:
            return values[0]
    else:
        #return None
    #    print len(values)
        return 'Not enough operators.'

#TESTS
assert True


if __name__ == "__main__":
    print '%s\n| RPN Calculator |\n%s'%('='*18,'='*18)
    help = ('Valid operators: + - * / ^\n' + 
     'Valid values: naturals and decimals, and\n' +
     '   Constants: phi\n' +
     'Commands: \'trace\', \'exit\', \'help\'')
    print help
    #help = 'Enter an expression, \'help\', or \'Exit\''
    #print help
    trace = False
    while True:
        s = raw_input('>> ')
        if 'exit' in string.lower(s):
            sys.exit()
        if 'help' in string.lower(s):
            print help
        elif 'trace' in string.lower(s):
            trace = not trace
            print '   [Trace mode now %s.]'%('on' if trace else 'off')
        else:
            print '   = %s'%rpcVal(s,trace)
