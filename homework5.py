mutable_list = ['one', 2, 3, 4]    # 'list', Список
print(mutable_list)
print(type(mutable_list))
print(mutable_list[0])
print(type(mutable_list[0]))
mutable_list [0] = int(1)
print(mutable_list[0])
print(type(mutable_list[0]))
print(mutable_list)
mutable_list.append('yellow')  # add var
print(mutable_list)
mutable_list.remove('yellow') # delete var
immutable_var = (mutable_list,[5 ,6 ,7], 8, 9, '0')  # 'tuple', Кортеж
print(immutable_var)
print(immutable_var [0])
print(type(immutable_var [0]))
print(immutable_var[1])
print(type(immutable_var [1]))
print(immutable_var[2])
print(type(immutable_var [2]))
print(immutable_var[4])
print(type(immutable_var [4]))
immutable_var[0][0]= '1'
immutable_var[0][1]= '2'
immutable_var[0][2]= '3'
immutable_var[0][3]= '4'
immutable_var[1][0]= '5'
print('Mutable_list: ',mutable_list )
print('Immutable tuple:',immutable_var)