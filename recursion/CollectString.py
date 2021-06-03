obj={
    "staff":"foo",
    "data":{
        "val":{
            "info":"bar",
            "moreInfo":{
                "eventMoreInfo":{
                    "weMadeIt":"baz"
                }
            }
        }
        
    }
}

def collect_strings(obj):
    cs=[]
    for k,v in obj.items():
        if type(v)==str:
            cs.append(v)
        else:
            if type(v)==dict:
                return cs + collect_strings(v)
    return cs

def collect_strings2(obj):
    result_arr = []
    for key in obj:
        if type(obj[key]) is str:
            result_arr.append(obj[key])
        if type(obj[key]) is dict:
            result_arr = result_arr + collect_strings2(obj[key])
    return result_arr

print(collect_strings(obj))