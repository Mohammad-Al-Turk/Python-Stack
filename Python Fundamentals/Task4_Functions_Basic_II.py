# 1. #CountDown
# def CountDown(number):
#     arr=[]
#     for i in range(1 , number+1 , 1):
#         arr.append(i)
#     return arr
# list=CountDown(5)
# print(list)



# #2. Print and Return
# def print_and_return(value1,value2):
#     print(value1)
#     return value2
# result = print_and_return(2,3)
# print(result)



#2. Print and Return  حل بطريقه ثانيه كمان هو مطلوب
# def print_and_return(value1):
#     print(value1[0])
#     return value1[1]
# result = print_and_return([2,3])
# print(result)


# #3. First Plus Length
# def first_plus_length(element):
#     sum = len(element) + element[0]
#     return sum
# result = first_plus_length([1,2,3,4,5])
# print(result)


# #4. Values Greater than Second
# def values_greater_than_second(element):
#     arr = element
#     grater=[]
#     for i in range(0,len(arr)):
#         if arr[i] > arr[1]:
#             grater.append(arr[i])
#     if len(grater) > 2:
#         print(len(grater))
#         return grater
#     else:
#         return False

# result = values_greater_than_second([1,2,3,3,4])
# print(result)


# #5. This Length, That Value
# def thislength_that_value(size , value):
#     arr=[]
#     for i in range(0,size,1):
#         arr.append(value)
#     return arr
# result=thislength_that_value(6,2)
# print(result)