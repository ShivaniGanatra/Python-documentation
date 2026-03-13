# f string
user_name = "Anna"
user_age = 25

user_information = f'{user_name} is {10 + user_age} years old'
print(user_information)

#single line if statements

user_status = 'Adult' if user_age >= 18 else 'Child'
print( f'{user_name} is {user_age} years old. The person is a {'Adult' if user_age >= 18 else 'Child'} ' )

# list comprehension

simple_list = []
for i in range(0,10,1):
    simple_list.append(i)
print(simple_list)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

simple_even_list = []
for i in range(0,10,2):
    simple_even_list.append(i)
print(simple_even_list)
# [0, 2, 4, 6, 8]

a_different_list = [f'{j}{i}' for i in range(0,5,1) for j in ("a","b","c")]
print(a_different_list)
# ['a0', 'b0', 'c0', 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4']

a_different_list_to_before = [f'{j}{i}' for i in range(0,5,1) for j in ("a","b","c") if j == "a"]
print(a_different_list_to_before)
# ['a0', 'b0', 'c0', 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4']

double_value = lambda num: num * 2
print(double_value(10))

random_list = [1,2,343,56,3]
sorted_list = sorted(random_list)
print(sorted_list)

battleShipBoard = [f'{j}{i}' for i in range(1,6) for j in ("A","B","C","D","E")]
battleShipBoard.remove("C3")
print(battleShipBoard)

battleShipBoard2 = [f'{j}{i}' for i in range(1,6) for j in ("A","B","C","D","E") if f'{j}{i}' != 'C3']
print(battleShipBoard2)