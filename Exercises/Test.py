logs= [(1,1,'open'),(2,2,'open'),(1,3,'close'),(1,4,'open'),(1,6,'close'),(2,8,'close')]

dict_log=dict()
for i in logs:
    k= str(i[0]) + '-' + str(i[1])
    v= i[2]
    dict_log[k]=v

for k,v in dict_log.items():
    print(k,v)

dict_ordered= {k:v for k,v in sorted(dict_log.items(),key=lambda item:item[0])}
print(dict_ordered)

for k,v in dict_ordered:
    