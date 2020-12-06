list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
k1=[(x,y) for x in list1 for y in list2 if x+y==0]
print(k1)