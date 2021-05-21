
def sum_digits(n):
    assert  int(n)==n and int(n)>=0, 'Fail'
    if n == 0:  
       return 0
    else:
       return (n%10) + sum_digits(n//10) 

print(sum_digits(-1))
 