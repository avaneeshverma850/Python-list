l1=[]
print(type(l1))
l2=[1,2,3,"Avaneesh"]
print(l2)
l3=[1,2,3,4]
print(l3)
l4=[500,20,80,10,60,40]
print(l4[-1])
print(l4[-2])
print(l4[-3])
print(l4[-4])
print(l4)
"""for i in l4:
    print(i,end=' ')
print()
i=0
while i<len(l4):
    print(l4[i],end=' ')
    i=i+1"""
#Editing list element put valid index value
l4[2]=15
print(l4)
print(l4.insert(2,10))
print(l4)
l4.append(100)
print(l4)
l4.insert(3,145)
print(l4)
#packing and unpacking
l1=[20,50,30]
a,b,c=l1
print(l1)
a=5
b=4
c=2
l2=[a,b,c]
print(l2)
print(len(l2))
print(min(l2))
print(max(l2))
print(sum(l2))
print(sorted(l2))
l=[12,14,True,"Avaneesh"]
#list method
l1=list()
print(type(l1))
l=[10]
print(type(l))
print(l)
l1=list("Mysirg")
print(l1)
print(list(range(5)))
print(list([10,20,30]))
print(list[1,2,3,4])
l=list([1,2,3,4,5,6,7,8])
print(l)
#Comparsion operator on list
l1=[1,2,3]
l2=[2,3,1]
l3=[1,2,3,4,5]
l4=[1,2,3]
print(l1==l4)
print(l1==l3)
print(l1==l2)
print(l1<l2)
#Repetition operator
print(l1*2)
print(l1)
l1=[20,40,10,30,60,50]
print(l1[::-1])
print(l1[::1])
print(l1[::2])
print(l1[::-2])
print(l1[1::])
#list of list
l1=[[1,2,4],[2,3,1],[5,4,3]]
print(l1[0][0])
print(l1[0][1])
print(l1[0][2])
print(l1[1][0])
print(l1[1][1])
print(l1[1][2])
#list object method
l1=[50,70,30,80,10,60,40,100,70]
"""del l1[1]
print(l1)"""
l1.remove(70)
print(l1)
"""l1.remove(120)
print(l1)"""
#remove last element
#it will return the last element
l1.pop()
print(l1.pop())
l1.pop(-2)
print(l1)
l1=[50,70,30,80,10,60,40,100,70]
print(l1.index(70))
print(l1.count(70))
#list comprehension
print([x**2+1 for x in range (1,6)])
#user input
"""l3=list(input("enter string:")) #Wrong method
print(l3)"""
"""print("How many number you want to enter")
n=int(input())
l1=[]
i=0
while i<n:
    l1.append(input("Enter a numnber:"))
    i=i+1
print(l1)"""
#wap to calulate sum of elements of a list
l=[1,2,3,4,5]
print(sum(l))
#Another method 
sum=0
for i in l:
    sum=sum+i
print(sum)
#write python script to calculate average of elemnt of list
l=[1,2,3,4,5,6]
print(len(l))
#another method
sum=0
for i in l:
    sum=sum+i
print(sum/len(l))
#python script to create a list of square of number of a given list
l=[1,2,3,4,5,6]
for i in l:
    print(i**2,end=' ')
print()
#write a python script to sort list element in descending orde
l=[1,2,3,4,5,6,7,8]
print(sorted(l))
print(l[::-1])
#WAP to create a list from a given list by selectng only even places
l=[1,2,3,4,5,6,7,8,9,10,12,14,13,14,15,16,17,18,19,20]
print(l[1::2])
#another method will be
#WAP to create a list of first n even natural numbers
"""x=int(input("Please enter a number:"))
l=[]
for i in range(0,x+1):
    if (i%2==0):
        l.append(i)
print(l)"""
#Write a python script create two list from given
"""x=int(input("Please enter number:"))
l1=[]
l2=[]
for i in range(0,x+1):
    x=int(input("enter number:"))
    if x>0:
        l1.append(x)
    else:
        l2.append(x)
print(l1)
print(l2)"""
#WAP create a list of first n prime numbers
"""print("Welcome here to print prime number")
l=[]
x=int(input("Please enter lower limit:"))
y=int(input("please enter upper limit:"))
for j in range(x,y+1):
    if j==1 or j==0:
      print("It is Not Prime Number")
    else:
     for i in range(2,j):
       if (j%i==0):
        break
     else:
      l.append(j)
print(l)"""
#write a python script to add two matrices each of order 3*3
"""print("Welcome here to display a matrix")
x=int(input("Enter number of rows:"))
y=int(input("Enter number of columns:"))
l1=[]
for i in range(0,x):
    for j in range(0,y):
        z=int(input("Please enter number:"))
        l.append(z)
print(l)"""
#write a python script to add two matrices each of order 3*3
matrix = []
for i in range(3):
        row = []
        for j in range(3):
            # You can modify this line to take input from the user if needed
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
            matrix.append(row)
print(matrix)
