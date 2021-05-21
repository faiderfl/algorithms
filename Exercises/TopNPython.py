
import sys
import collections

line='video,cs101,meta,bug,issues,nationalities,cs101,welcome,cs101,cs212,cs262,discussion,meta'


words = line.split(",")
counter = collections.Counter(words)
print(counter)
'''
for line in words:
    k = line
    counter[k] += 1
'''

print (counter.most_common(2))  