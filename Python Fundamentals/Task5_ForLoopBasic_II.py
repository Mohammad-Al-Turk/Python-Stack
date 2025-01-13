#1. Biggie Size
# arr=[-1,5,6,-6]
# for i in range(len(arr)):
#     if arr[i] < 0:
#         arr[i]="big"
# print(arr)


# #2. Count Positives
# arr=[1,6,-4,-2,-7,2]
# count =0
# for i in range(0 , len(arr)):
#     if arr[i] > 0 :
#         count=count+1
# arr[i]=count
# print(arr)


# # 3. Sum Total
# arr=[1,6,-4,-2,-7,2]
# count =0
# for i in range(0 , len(arr)):
#     count=count+arr[i]
# print(count)


#4. Average
# sum=0
# avg=0
# count = 0 
# arr=[1,2,3,4]
# for i in range(0,len(arr)):
#     sum=sum + arr[i]
#     count=count+1
# print("the sum =" ,sum)
# print("number of number=" ,count)
# avg = sum / count
# print("the avg =" ,avg)


# #5. Length 
# arr=[2,3,4,5]
# count= 0
# for i in range(0,len(arr)):
#     count = count +1
# print(count)    


#6. Minimum
# arr=[]
# neg_nums = float('inf')

# if len(arr) == 0:
#        print("False")
# else:
#     for i in range(0,len(arr)):
#         if arr[i] < neg_nums :
#             neg_nums = arr[i]
#     print(neg_nums)

    
# #7. maximum
# arr=[]
# neg_nums = 0

# if len(arr) == 0:
#        print("False")
# else:
#     for i in range(0,len(arr)):
#         if arr[i] > neg_nums :
#             neg_nums = arr[i]
#     print(neg_nums)


#8. Altimate


# #9. Reverse
# arr=[2,3,4,5,6]
# pointer=len(arr)-1
# temp=0
# for i in range(0, len(arr)//2 ,1):
#     temp=arr[i]
#     arr[i] = arr[pointer]
#     arr[pointer] = temp
#     pointer=pointer-1
# print(arr)