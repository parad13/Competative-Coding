data = [3, 4, 5]
data1 = (3, 4, 5)

# dict1 = {data : "dsf"} # Can't assign a list as a key in dict as its immutable #TypeError: unhashable type: 'list'
dict2 = {data1 : "dsf"} 

# print(dict1) #TypeError: unhashable type: 'list'
print(dict2)

print(dict2[data1])
print(dict2.keys())