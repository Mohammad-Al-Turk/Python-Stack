arr=[3,5,7,9,1,6,4,8,2]

for i in range(0,len(arr)):
    for x in range(0,len(arr)):
        if arr[x] > arr[i]:
            temp = arr[x]
            arr[x] = arr[i]
            arr[i] = temp
        
print(arr)
    