def capitalize_first(arr):
    len_arr=len(arr)
    if len(arr)==1:
        aux=''
        aux=arr[len_arr-1][0].upper()
        aux = aux+ arr[len_arr-1][1:]
        arr[len_arr-1]=aux
        return [arr[len_arr-1]]
    else:
        aux=''
        aux=arr[0][0].upper()
        aux= aux + arr[0][1:]
        arr[0]=aux  
        return [arr[0]] + capitalize_first(arr[1:])

print(capitalize_first(['car','taco','banana']))


def capitalize_first2(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalize_first2(arr[1:]) 

print(capitalize_first2(['car','taco','banana']))