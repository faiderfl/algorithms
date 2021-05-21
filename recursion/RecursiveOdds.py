def is_odd(num)->bool:
    if num%2==0:
        return False
    else:
        return True
        
def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if len(arr)==1:
        return cb(arr[0])
    else:
        if cb(arr[len(arr)-1]):
            return True         
        else:
            return some_recursive(arr[:len(arr)-1],cb)

def some_recursive2(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1:], cb)
    return True


print(some_recursive([1,2,3,4], is_odd))
print(some_recursive([4,6,8,9], is_odd))
print(some_recursive([4,6,8], is_odd))

print(some_recursive2([4,6,8], is_odd))