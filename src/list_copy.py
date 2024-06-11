x=[10, 30, 2, 44, 25, 15, 35, 1,33, 11]
y=x

print(x)
print(id(x))
print(y)
print(id(y))
x[2]=0 # it will update the value in both the list x and y because it point to the same memory address
print(x)
print(y)

c=x.copy()
print(id(c))
print(id(x))
x[1]=45
c[1]=100
print(x)
print(c)

#MEMBERSHIP OPERATORS IN PYTHON (IN /NOT IN), Answer will be in Boolean as it return true or false

x=[10, 30, 2, 44,"farheen", 25, 15, 35, 1,33, 11]
print("farheen" in x)
print(100 in x)
print(100 not in x)

#Create the list and delete the duplicate elements
x=[10, 10,30, 2, 44,"farheen", 25, 15, 35, 1,33, 11,11,10]
y=[]
for i in x:
    if (i not in y):
        y.append(i)
print(y)
#new_lst = [i for i in x if i % 10 != 0]

num= int(input("Enter the number"))
if(num in y):
    print(y.index(num))
else:
    print(-1)




