obj={
    "num":1,
    "test":[],
    "data":{
        "val":4,
        "info":{
            "isRight":True,
            "random":66
        }
    }
}

def stringify_numbers(obj):
    new_obj= obj
    for k,v in obj.items():   
        if type(v)== int:
            new_obj[k]=str(v)
    
        else:
            if type(v)==dict:
                new_obj[k]= stringify_numbers(v)
                 
    return new_obj


def stringify_numbers2(obj):
    new_obj = obj
    for key in new_obj:
        if type(new_obj[key]) is int:
            new_obj[key] = str(new_obj[key])
        if type(new_obj[key]) is dict:
            new_obj[key] = stringify_numbers2(new_obj[key])
    return new_obj


print(stringify_numbers(obj))