#list set dictionnary
# simple_dict = {
#         'a':1,
#         'b': 2
# }
# my_dict = {key:v**2 for key,v in simple_dict.items() if v%2==0}

# print(my_dict)#output:{'a': 1, 'b': 4} if u add (ifv%2==0)output:{'b': 4}
#--------------------------------------------------------------------------------
# my_dict = {num:num+2 for num in [1,2,3]}
# print(my_dict)#output:{1: 3, 2: 4, 3: 5}
#--------------------- return a list of duplicate----------------------------------------
some_list = ['a','b','c','b', 'd','m','n','n']

# duplicates = [x for x in some_list if some_list.count(x)>1]
# for value in some_list:
#         if some_list.count(value)>1:
#                 if value not in duplicates:
#                         duplicates.append(value)
# print(duplicates) output [n]
# print(duplicates)#output ['b', 'b', 'n', 'n']
#---------------------------------------------------------------
# duplicates = set([x for x in some_list if some_list.count(x)>1])
# print(duplicates)#output : {'b', 'n'}
#----------------------------------------------------------------
duplicates = list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicates)#output:['n', 'b']
#------------------------------------------------------------------
