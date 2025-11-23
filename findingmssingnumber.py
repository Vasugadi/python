ar=[1,2,4,5,6,7]
n=len(ar)+1
total_sum=n*(n+1)//2
array_sum=sum(ar)
missing_number=total_sum - array_sum
print("The missing number is:",missing_number)

#another method
def find_missing_number(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i
    return None
arr = [1, 2, 4, 5, 6, 7]
n = len(arr) + 1

#another method using xor
xor_all = 0
xor_arr = 0
for i in range(1, n + 1):
    xor_all ^= i
for num in arr:
    xor_arr ^= num
missing_number = xor_all ^ xor_arr
print("The missing number is:", missing_number)

#
def getmissingnumber(arr, n):
    n=len(arr)
    xor_all = arr[0]
    print(xor_all)
    for i in range(1, n):
        print(arr[i])
        xor_all ^= arr[i]
    x2=0
    for i in range(len(arr)+2):
        x2 ^= i
    return xor_all ^ x2
arr = [1, 2, 4, 5, 6, 7]
n = len(arr) + 1
print("The missing number is:", getmissingnumber(arr, n))