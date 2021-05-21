def product_of_array(arr)->int:
    """Function wich takes an array of numbers and returns the product of them all.

    Args:
        arr ([int]): numbers

    Returns:
        int: product of numbers inside arr
    """    

    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]* product_of_array(arr[1:])

print(product_of_array([1,2,3]))
print(product_of_array([1,2,3,10]))