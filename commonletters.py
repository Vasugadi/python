str=input("Enter first string: ")
str2=input("Enter second string: ")
common_letters=set(str).intersection(set(str2))
print("Common letters:", common_letters)

#by using loops
common_letters_loop=[]
for letter in str:
    if letter in str2 and letter not in common_letters_loop:
        common_letters_loop.append(letter)
print("Common letters using loops:", common_letters_loop)

#how to remove duplicates from  a string
input_str=input("Enter a string with duplicates: ")
s1=set(input_str)
input_str2=input("Enter another string with duplicates: ")
s2=set(input_str2)
print(s1 & s2)
common_letters_no_duplicates=s1.intersection(s2)
print("Common letters without duplicates:", common_letters_no_duplicates)