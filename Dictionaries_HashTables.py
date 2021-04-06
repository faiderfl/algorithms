car={
    "brand":"Ford",
    "model":"Mustang",
    "year": 1963,
    "year": 2020    
}

print(car)
print(len(car))
for k,v in car.items():
    print (k,v)

if 'brand' in car:  # Check key
    print('\nBrand:', car['brand']) # 'Ford'


dic2 = dict((('mesa',5), ('silla',10)))
dic3 = dict(ALM=5, CAD=10)
dic4 = dict([(z, z**2) for z in (1, 2, 3)]) 
print (dic4)


print(car.items())  #Key:Value
print(car.keys())   # Keys
print(car.values()) #Values