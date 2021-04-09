
import sys
import collections

counter = collections.Counter()
line='video,cs101,meta,bug,issues,nationalities,cs101,welcome,cs101,cs212,cs262,discussion,meta'
words = line.split(",")
for line in words:
    k = line
    counter[k] += 1

print (counter.most_common(10))  