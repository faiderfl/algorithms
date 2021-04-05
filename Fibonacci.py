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


if __name__ == "__main__":
    print(fibonacci_Recursive(7))
    print(fibonacci_Itarative(7))
