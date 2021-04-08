import re
book= 'Hola Faider, HOLA Juan, Hola Mundo, Hola Pedro Faider'
book= book.lower()

words=[]

#book= book.replace('/[,.!]/g','')
book= re.sub('[,.!]','',book)
words= book.split(' ')

count = dict()
for i in words:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1

for k,v in count.items():
 print (k,v)