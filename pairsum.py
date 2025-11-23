def two_sum(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]>target:
            right-=1
        
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            print("value of pair are:",arr[left],arr[right])
            right-=1
            left+=1

print(two_sum([1,2,3,4,5],7))
