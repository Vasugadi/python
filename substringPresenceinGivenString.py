str="welcome to python programming"

sub_str="python"

if sub_str in str:
    print("present")
else:
    print("not present")
    
#or
print(str.find(sub_str))
#str.find(sub_str)>-1 means if the substring is present in the string then it will return the index of the first character of the substring in the string
if str.find(sub_str)>-1:
    print("present")
else:
    print("not present")
    


