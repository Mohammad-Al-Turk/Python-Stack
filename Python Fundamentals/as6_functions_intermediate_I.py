import random
# def random_int(num1,num2):
#     get_random_num = random.randint(num1, num2)
#     return get_random_num
# result = random_int(0,100)
# print(result)    
    
    

def randInt(min= 0, max= 100):
    num = random.randint(min,max)
    return num


#print(randInt(0 , 100))             # should print a random integer between 0 to 100
# print(randInt(max=50))         # should print a random integer between 0 to 50
# print(randInt(min=50))         # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500