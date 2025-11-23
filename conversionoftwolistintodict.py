list1=["naina", "rahul", "sonam"]
list2=[21, 22, 20]
dict1={}
for i in range(len(list1)):
    dict1[list1[i]]=list2[i]
print(dict1)

#using zip function
dict2=dict(zip(list1, list2))
print(dict2)
for i in dict2.items():
    print(i)