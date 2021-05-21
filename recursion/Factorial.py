import sys
sys.setrecursionlimit(1000)

#n>0
def factorial(n):
    assert n>=0 and int(n)==n, 'The number must be possitive integer only'
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
