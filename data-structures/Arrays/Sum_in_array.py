from Utilities.Elapsed_Time import count_elapsed_time

numbers = [1,2,3,4,5,6,7]
print (numbers)

@count_elapsed_time
def sum_in_array_recursive(numbers,n):
    if n==1:
        return numbers[0]
    
    s= sum_in_array_recursive(numbers,n-1)
    s= s + numbers[n-1]
    
    return s

@count_elapsed_time
def sum_in_array_iterative(numbers,n):
    s=0 
    for i in range(0,n):
        s= s + numbers[i]
    return s

if __name__=="__main__":
    print(sum_in_array_recursive(numbers,7))
    print(sum_in_array_iterative(numbers,7))