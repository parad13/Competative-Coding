data = [3, 4, 5]

# Method 1 - Wrong one
doubled_data1 = data * 2
print(doubled_data1)

# Method 2
doubled_data2 = []
for i in data:
    doubled_data2.append(2*i)
print(doubled_data2)

# Method 3
doubled_data3 = [2*x for x in data]
print(doubled_data3)