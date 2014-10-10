#twentysix.py
'''
Uses the RPN Calculator to solve this specific problem:

Using each the numbers 2,3,4 & 5 exactly once, and at
most one each of +,-,*,/, get 26 as a result.
'''

from itertools import permutations
from polish_calc import rpcVal

nums = ['2','3','4','5']

ops = ['+','-','*','/']

target = 0#26
while target < 30:
    p_nums = set([''.join(p) for p in permutations(''.join(nums))])
    p_ops = set([''.join(p)[:3] for p in permutations(''.join(ops))])

    results = set()
    for np in set(p_nums):
        for op in set(p_ops):
            s = ''
            for e in np:
                s+=e+' '
            for e in op:
                s+=e+' '
            s = s[:-1]
            result = rpcVal(s)
            if result != None and result == target:
                if result not in results:
                    results.add(result)
                    print '%s = %d'%(s,result)
    target += 1