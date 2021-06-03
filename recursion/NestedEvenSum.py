obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

obj3 = {
  "a": 2,
  "b": 3,
  "c": 2,
  "d": 1,
  "e": 4
}


def nested_even_sum(obj, sum_=0):
    aux_dic=obj.copy()
    for k,v in obj.items():
        if type(v)==int:
            if v%2==0:
                sum_=sum_+v
            aux_dic.pop(k)
        elif type(v)==dict:
            aux=v
            aux_dic.pop(k)
            aux_dic.update(aux)
            return nested_even_sum(aux_dic,sum_)
        else:
            aux_dic.pop(k)
            return nested_even_sum(aux_dic,sum_)
    return sum_
        

def nested_even_sum2(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nested_even_sum2(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum


print(nested_even_sum(obj1))
print(nested_even_sum(obj2)) 
print(nested_even_sum(obj3))     