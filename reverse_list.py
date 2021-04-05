li= (1,2), (1, 3), (2,1), (1,4), (4, 2), (2, 3), (2, 4)

li_ordered= sorted(li, key=lambda tup: tup[0])
li_reverse=[]

for p in li_ordered:
    if (p[::-1]) in li_ordered and p[::-1] not in li_reverse:
        li_reverse.append(p)

print(li_reverse)

