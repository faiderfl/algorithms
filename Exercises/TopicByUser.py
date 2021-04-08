from collections import Counter

topicbyUser= [('User1','Topic1'),('User1','Topic2'),('User2','Topic1'),('User2','Topic3')]
#print(type(topicbyUser))
#print (topicbyUser[0][0])

#dict_topicByUser = dict((x,y) for x,y in topicbyUser)

#for k,v in dict_topicByUser.items():
#    print(k,v) 

dict_topic= dict()
for u,t in topicbyUser:
    if t in dict_topic:
        dict_topic[t]=dict_topic[t]+1
    else:
        dict_topic[t]=1

#print(dict_topic)
dict_ordered= {k:v for k, v in sorted(dict_topic.items(), key=lambda item: item[0], reverse=True)}
#print(dict_ordered)

first2pairs = {k: dict_ordered[k] for k in list(dict_ordered)[:2]}
print(dict_topic.items())

dict_reduced= Counter(dict_ordered)
dict_filtered= list(dict_reduced.items())
print(dict_filtered[::-1][0:2])