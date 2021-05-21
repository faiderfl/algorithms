def is_odd(num)->bool:
    if num%2==0:
        return False
    else:
        return True
        
def some_recursive(arr, cb):
    if len(arr)==1:
        return cb(arr[0])
    else:
        if cb(arr[len(arr)-1]):
            return True         
        else:
            return some_recursive(arr[:len(arr)-1],cb)

print(some_recursive([1,2,3,4], is_odd))
print(some_recursive([4,6,8,9], is_odd))
print(some_recursive([4,6,8], is_odd))
