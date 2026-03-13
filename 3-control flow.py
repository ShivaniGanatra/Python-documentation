if 5 > 4:
    print('correct result') # this has to be indented

if (3> 4): 
    print("correct")
elif 2>1 :
    print("another result")
else :
    print("incorrect")

# while loop
counter = 0
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 5:
        print("counter is 5")
print("while loop has finished")
# prints 1 to 10    

# for loop
test_list = [1,2,3,4,5]
for x in test_list:
    print(x)

#prints 1 to 5

dictionairy = {1:2, 3:4, 5:6}
for x in dictionairy:
    print(x)
#prints 1 ,3 ,5 which are all the keys in the dictionairy

print("dictionairy keys")
for x in dictionairy.keys():
    print(x)
# prints 1 3 5

print("dictionairy values")
for x in dictionairy.values():
    print(x)
# prints 2 4 6 

print("dictionairy items")
for x in dictionairy.items():
    print(x)
   #you get tuple/s with key value pairs 
# (1, 2)
# (3, 4)
# (5, 6)

print("dictionairy items")
for k,v in dictionairy.items():
    print("key: ")
    print(k)
    print("value: ")
    print(v)
# key:
# 1
# value:
# 2
# key:
# 3
# value:
# 4
# key:
# 5
# value:
# 6

if 1:
    print("truthy")
else: 
    print("falsy")
#falsy - empty container, string without letters and 0 are False

print("excercise")
excerciseList = [1,2,3,4,5]

for x in excerciseList:
    aCounter = 0
    if x == 2: 
        print("value is 2")
    elif x == 5:
        while aCounter < 6:
            aCounter += 1
            print("last item")  
    else :
        print("value is not 2")


 