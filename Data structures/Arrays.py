#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered and changeable. No duplicate members.

#List
print ('----LIST----')
my_list= [1,2,3,4,'Hola',1]

my_list.append(5)
print(my_list)
my_list.pop(0)
print(my_list)
print(my_list[0:3:2]) #start:end:step
print(my_list[::-1])  #Reverse list

my_list.remove(4)
del my_list[1]
my_list.extend([8, 9])
my_list.insert(1, 'dos')
print(my_list.index("dos"))

my_list1=[5,4,3,2,1]
my_list2=[6,7,8,9,10]

my_list1.sort()  # Sort list in place
my_list1.sort(reverse=True)  # Sort list reverse in place
listaSorted = sorted(my_list1) #Sorted using TimSort

for i, c in enumerate(listaSorted): print(i,':',c)  
for p, c in zip(my_list1, my_list2): print(c,' ',p) 

for p, c in zip(my_list1, my_list2): print(p-c) 


my_list3 = my_list2.copy()

#Strings = List
print ('-----STRINGS----')
my_string= 'Hola Mundo Hola'
print(my_string.count('o'))
print(my_string.find('H'))
my_string = my_string + 'MMMM'
print(my_string)




#Tuples
print ('-----TUPLES----')
my_tupla=(1,2,3,4,'Hola',1)
print(my_tupla[0::4])
#my_tupla.append(5) -- Fail because it is unmutable


#SET
print ('-----SET----')
my_set = { 1,2,3,4,'Hola',1}
my_set.add(6)
my_set.remove('Hola') 
print(my_set) # No duplicates.
#print(my_set[1]) --Fail because set is unordered and unidexed