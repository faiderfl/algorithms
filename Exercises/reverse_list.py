li= (1,2), (1, 3), (2,1), (1,4), (4, 2), (2, 3), (2, 4)

li_ordered= sorted(li, key=lambda tup: tup[0])
li_reverse=[]

for p in li_ordered:
    if (p[::-1]) in li_ordered and p[::-1] not in li_reverse:
        li_reverse.append(p)

print(li_reverse)


dict_list= dict((x,y) for (x,y) in li)
print (dict_list)

dict_ordered= {k:v for k, v in sorted(dict_list.items(), key=lambda item: item[0], reverse=True)}
print(dict_ordered)