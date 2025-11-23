str=input("Enter a string: ")
list=str.split(" ")
d={}
for i in list:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print("Frequency of words in the given string:",d)

