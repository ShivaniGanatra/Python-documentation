a_tuple = (1,2,3,"a string") 
print(a_tuple)

a_list = [1,2,3, "a string",4,4,4]
print(a_list)
print(len(a_list))

a_list.append("another word")
print(a_list)

# List can be changed but a tuple cannot be changed

#In a set evrthing has to be unique
a_set = {1,2,3,4}

# To get rid of duplicates ina list you can turn it into a set
print(a_list)
print(set(a_list))

a_dictionairy = {"key": "Value",123 : [123]}
print(a_dictionairy) 

# how to get values for a container
#             0       1      2        3        4
#             -5      -4     -3       -2       -1
user_list = ["lisa","bob", "alex" , "anna", "john"]
print(user_list[0]) # gets first value
print(user_list[-5]) # gets first value
print(user_list[0:3]) 

anotherList = [1,2,3,4,5,6,7,8,9,10]
newList = anotherList[1: 8: 2]
print("new list")
newList.reverse()
print(newList)
# [8, 6, 4, 2]

differentList = anotherList[7::-2] # same as anotherList[7:0:-2]
print(differentList)