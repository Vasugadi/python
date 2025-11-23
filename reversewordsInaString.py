#input
str="welcome to python"
rev_str=str[::-1]
print(rev_str)
if str==rev_str:
    print("palindrome")
else:
    print("not palindrome")
    
#
s="welcome to python programming"
words=s.split()
words=words[-1::-1]
print(words)
output=" ".join(words)
print(output)

#