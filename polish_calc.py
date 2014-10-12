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

'''
TO BE IMPLEMENTED:

a b c quad1: rpcVal('0 b - b ^ 2 4 a c * * - 1 2 / ^ - 2 a * /',trace)
a b c quad2: rpcVal('0 b - b ^ 2 4 a c * * - 1 2 / ^ + 2 a * /',trace)

x y w z dist: rpcVal('x w - 2 ^ y z - 2 ^ + 1 2 / ^',trace)
x y hyp:  rpcVal('x 2 ^ y 2 ^ 1 2 / ^',trace)
        = rpcVal('x y 0 0 dist',trace) 

a b amean = rpcVal('a b + 2 /',trace)
a b gmean = rpcVal('a b * 1 2 / ^',trace)
'''

def isNum(s):
    s = str(s)
    if s.count('.')>1: return False
    d = string.digits+'.'
    for c in s:
        if c not in d:
            return False
    return True

def isWhole(num):
    return (abs(num-float(int(num)))<=1e-9)

def rpcVal(expr,trace):
    constants = ['e','pi','phi']
    unary = ['fib']
    binary = ['+','-','*','/','^']
    ternary = ['quad1', 'quad2', 'hyp','amean','gmean']
    tokens = expr.split()
    if len(tokens)==0:
        return 'Need at least one token.'
    if 'ops?' in expr:
        return [', '.join(constants),(', '.join(binary))+', '+(', '.join(unary))+', '+(', '.join(ternary))]
    values = []
    while len(tokens)>0:
        #recognized = False
        if trace:
            print ' - values: %s,\n   tokens: %s'%(values,tokens)
            #print ' - values: %s'%values
        c = tokens[0]
        if isNum(c): #number (natural or decimal)
            values.append(float(c))
        elif c=='e':
            values.append(rpcVal('1 1 10 11 ^ / + 10 11 ^ ^',trace))
        elif c=='pi':
            values.append(rpcVal('245850922 78256779 /',trace))
        elif c=='phi': #constant
            values.append(rpcVal('5 1 2 / ^ 1 + 2 /',trace))
        elif len(values)==0: return 'At least one value is needed.'#for %s.'%c
        #elif len(values)>=1: #unary operators
        else:
            if len(values)>=1: #unary operators
                if c=='fib': # overflows if argument > 1474
                    values = values[:-2]+[rpcVal('phi %s ^ 0 phi - 0 %s - ^ - 5 1 2 / ^ /'%(values[-1],values[-1]),trace)]
                #elif c in unary:
                #    return 'Not enough values for %s.'%c
                #else:
                #    return 'Unrecognized symbol: %s.'%c
                if len(values)>=2: #binary operators
                    if c=='+':
                        #print 'Time to add.'
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
                        b,p = values[-2],values[-1]
                        if b<0 and not isWhole(p):
                            return 'Error: negative raised to fractional power.'
                        else:
                            values = values[:-2]+[b**p]
                    elif c=='hyp':
                        pattern = '%s 2 ^ %s 2 ^ + 1 2 / ^'%(values[-2],values[-1])
                        result = rpcVal(pattern,trace)
                        if type(result) == str: return result
                        else: values = values[:-2]+[result]
                    elif c=='amean':
                        pattern = '%s %s + 2 /'%(values[-2],values[-1])
                        result = rpcVal(pattern,trace)
                        if type(result) == str: return result
                        else: values = values[:-2]+[result]
                    elif c=='gmean':
                        pattern = '%s %s * 1 2 / ^'%(values[-2],values[-1])
                        result = rpcVal(pattern,trace)
                        if type(result) == str: return result
                        else: values = values[:-2]+[result]
                    #else:
                    #    if c in unary:
                    #        return '%s needs an argument.'%c
                    if len(values)>=3: #ternary operators
                        if c=='quad1':
                            a,b,c = values[-3],values[-2],values[-1]
                            pattern = '0 %s - %s 2 ^ 4 %s %s * * - 0.5 ^ - 2 %s * /'%(b,b,a,c,a)
                            result = rpcVal(pattern,trace)
                            if type(result) == str: return result
                            else: values = values[:-3]+[result]
                        if c=='quad2':
                            a,b,c = values[-3],values[-2],values[-1]
                            pattern = '0 %s - %s 2 ^ 4 %s %s * * - 0.5 ^ + 2 %s * /'%(b,b,a,c,a)
                            result = rpcVal(pattern,trace)
                            if type(result) == str: return result
                            else: values = values[:-3]+[result]
        '''
        if c in binary+ternary:
            return 'Not enough values for %s.'%c
        else:
            return 'Unrecognized symbol: \'%s\'.'%c
        '''
        tokens = tokens[1:]
    #print 'tokens empty.'
    
    #if trace: print 'tokens: %s, values: %s'%(tokens,values)
    if len(values)==1:
        #if abs(values[0]-float(int(values[0])))<=1e-9: #truncate if (almost) whole number
        if isWhole(values[0]):
            return int(values[0])
        else:
            return values[0]
    else:
        #return None
    #    print len(values)
        return 'Not enough operators.'

#TESTS
#assert (rpcVal('',False) == )
assert (rpcVal('',False) == 'Need at least one token.')
#assert (rpcVal('3 5 ^ 1 -',False) == 242)
#assert (rpcVal('6 1 / 0 *',False) == 0)
'''
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )
assert (rpcVal('',False) == )'''

if __name__ == "__main__":
    print '%s\n| RPN Calculator |\n%s'%('='*18,'='*18)
    ops = rpcVal('ops?',False)
    help = ('Valid operators: %s\n'%ops[1] + 
     'Valid values: naturals and decimals, and\n' +
     (' '*14)+'Constants: %s\n'%ops[0] +
     'Commands: \'trace\', \'exit\', \'help\'')
    print help
    #help = 'Enter an expression, \'help\', or \'Exit\''
    #print help
    trace = False
    while True:
        s = raw_input('>> ')
        low = string.lower(s)
        if 'exit' in low or 'quit' in low:
            sys.exit()
        if 'help' in low:
            print help
        elif 'trace' in low:
            trace = not trace
            print '   [Trace mode now %s.]'%('on' if trace else 'off')
        else:
            print '   = %s'%rpcVal(s,trace)
