import numpy as np
# !D Arraay Also known as vector 
n1=np.array([12,14,15])
print(n1)

# 2D Array 
n2=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(n2)
print(type(n2))

#initializing Array with Zeros
n3=np.zeros((1,2))
print(n3)
n4 =np.zeros((3,3))
print(n4)

#initializing Array with same Element 
n5=np.full((3,3),10)
print(n5)
nn=np.ones(3)
# unit Matrix 
n6=np.identity(3)
print(n6)

print(n6*2)

# arange numpyarray within range
n7=np.arange(10,50,5)# call First starting limit ,endding limit and gap / Incremen
print(n7)

n8=np.arange(10,50)# call First starting limit ,endding limit and gap / Incremen
print(n8)

n9=np.random.randint(1,100,5)
print(n9)

print(n2.shape)
n2.shape=(5,2)
print(n2)
#to concatate two matrixs
print(np.hstack((n4,n5)))
print(np.vstack((n4,n5)))
print(np.column_stack((n4,n5) ))

#Union and Intersection of arrays

n10=np.array([12,13,1,41,41,2,3,4,56])
n11=np.array([12,43,2,5,6,7,942,223])
print(np.intersect1d(n10,n11))
print(np.setdiff1d(n10,n11))

#additotn of 2 array
n10=np.array([range(20,31)])
n11=np.array([range(0,11)])

print(np.sum([n10,n11]))
print(np.sum([n10,n11],axis=0))
print(np.sum([n10,n11],axis=1))

#arathiamtic oration on array

print(n10+1)
print(n10-1)
print(n10*10)
print(n10/2)
print(n10**2)

#post lab practice 

#Task WAP to find the longest string in given list 
l1=["ICT","Department","ICT Department"]
long=l1[0]
for i in range(0,len(l1),1):
    if(long<l1[i]):
        long=l1[i]
print(long)

# WAP to fidn the sum of unit digit in a number
l2=[25,36]
sum=0
for i in range(0,2,1):
    temp=l2[i]%10
    sum=sum+temp
print(sum)

#WAP fto find the largest number from 3 number
def BigO3(num1,num2,num3):
    big=max(num1,num2,num3)
    return big 

x=BigO3(12,1,55)
print(x)

#task find the sum of all number from list
def ListSum(l11):
    sum=0
    for i in range(0,len(l11)+1,1):
        sum+=l11[0]
    return sum

Sums=ListSum([1,2,3,4,5,6,7,8,9])
print(Sums)