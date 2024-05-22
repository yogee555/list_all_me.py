# LIST METHOD
# APPEND [1]
a=[1,2,3]
a.append(4)
print(a)
#  APPEND [2]
d=[1,2,3]
d.append([4,5])
print(d)

# EXTEND [1]
b=[10,20,30,40]
c=[50,60,80,70,90,100]
b.extend(c)
print(b)
# EXTEND [2]
p=[1,2,3]
p.extend([4,5])
print(p)

# INSERT
n=['a','b','c','d']
n.insert(2,'h')
print(n)

# CLEAR
items=['yogi',1,2,3]
items.clear()
print(items)

# COPY
co=['a','b','c','d']
print('original:',co)
ni=co.copy()
print('after:',ni)

# COUNT
data = ['H','I','Y','O','G','E','E','S','H','K','P']
# Count element 'P'
count=data.count('P')
#print count
print('the count of P is :',count)
# Count element 'E'
count=data.count('E')
#print count
print('the count of E is :',count)

# REVERSE[1]
list=[1,2,3,4,5]
list.reverse()
print('using list reverse:',list)
# REVERSE[2]
li=['a','b','c']
print(li)
li2=li[::-1]
print(li2)

# REMOVE
go=['apple','mango','orange']
go.remove('mango')
print(go)

# SORT
my_list=['apple','mango','orange','banana']
my_nu=[2,5,1,3,6,5,7,4]
my_list.sort()
my_nu.sort()
print(my_list)
print(my_nu)

# POP[1]
pop=[1,2,3]
pop.pop()
print(pop)
# POP[2]
y=[1,2,3,4,5,6]
y.pop(3)
print(y)

# INDEX
n = [10,20,30,40,50]
print("list of index and value are")
for i in range(len(n)):
    print('index number=',i,'index value=',n[i])
