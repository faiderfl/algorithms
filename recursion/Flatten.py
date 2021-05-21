def flatten(arr):
    if not isinstance(arr[0],list):
        if len(arr)==1:
            return [arr[0]]
        else:
            return [arr[0]] + flatten(arr[1:])
    else:
        return flatten(arr[0][:] + arr[1:])

def flatten2(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 


print(flatten([[1]]))
print(flatten([1,[[2]]]))
print(flatten([1,2,3,[4,5]]))
print(flatten([1,[2,[3,4],[[6]]]]))

print(flatten2([1,[2,[3,4],[[6]]]]))