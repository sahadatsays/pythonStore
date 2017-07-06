from filecmp import cmp

tuple_1 = (2,3,4,6,2,1,3,4,2,1,20)
tuple_2 = (2,3,4,6,2,1,3,4,2,1)
print(tuple_1)

print(len(tuple_1))
print(max(tuple_1))
print(min(tuple_1))

newList = list(tuple_1)
print(newList)
print('New List from Tuple : ',newList)
newTuple = tuple(newList)
print('New Tuple', newTuple)