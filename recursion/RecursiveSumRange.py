
def recursive_sum_range(num)->int:
    """Function wich accepts a number and adds up all the numbers from cero to the number passed to the function

    Args:
        num (int): number up 

    Returns:
        int: sum of all number from cero to final number
    """    
    if num==0:
        return 0
    else:
        return num + recursive_sum_range(num-1)
    
print(recursive_sum_range(4))