#0,1,1,2,3,5,8,13
def fibonacci_Recursive(n):
    if n<=1:
        return n
    else:
        return fibonacci_Recursive(n-1)+fibonacci_Recursive(n-2)

def fibonacci_Iterative(n):
    fibo=[0,1]
    for i in range(2,n+1):
        fibo.append(fibo[i-2]  + fibo[i-1])
    return fibo[n]


def fibonacci_Dynamic(n,memo):
    if n in memo:
        return memo[n]
    else:    
        memo[n]= fibonacci_Dynamic(n-2,memo) + fibonacci_Dynamic(n-1, memo)
        return memo[n]

if __name__ == "__main__":
    print(fibonacci_Recursive(7))
    print(fibonacci_Iterative(7))
    print(fibonacci_Dynamic(40, {0:0,1:1}))

