#input=[1,6,3,5,3,4]
#output=[]


#approaches
"""
clear()
initialize a list with empty values
*=()
using del()
"""

#app1
mylist=[1,6,3,5,3,4]
print("my list before clear")
mylist.clear()
print("my list after clear")


#app2 
mylist=[1,6,3,5,3,4]
print("my list before clear",mylist)
mylist=[ ]
print("my list after clear",mylist)

#app3
#*=0 this method will removes all the values of the list
mylist=[1,6,3,5,3,4]
print("my list before clear",mylist)
mylist*=()#it means mylist=[ ] using *=() we are assigning empty list to mylist
print("my list after clear",mylist)

#app4
mylist=[1,6,3,5,3,4]
print("my list before clear",mylist)
#del mylist[:] u can use it for a range of values
del mylist[:]
print("my list after clear",mylist)















def clearList(input):
    input.clear()
    return input

list=[1,6,3,5,3,4]
print(clearList(list))


