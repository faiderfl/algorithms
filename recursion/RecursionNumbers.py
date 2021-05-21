def recursion_method(n):
    if n<1:
        print("n is less than 1")
    else:
        recursion_method(n-1)
        print(n)

recursion_method(4)

#######################################

def power_numbers_recursive(n):
    if n==0:
        return 1
    else:
        power = power_numbers_recursive(n-1)
        return power*2
        
print(power_numbers_recursive(5))

#######################################

def power_numbers_iterative(n):
    i=0
    power=1
    while(i<n):
        power = power*2
        i+=1
    return power

print(power_numbers_iterative(5))

    