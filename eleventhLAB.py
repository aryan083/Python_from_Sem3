import numpy as np
#broadCasting
a1=np.array([1,2,3,4])
a2=np.array([[5],[6],[7],[8]])
sum=a1+a2
print(sum)
#print squres matries 
#2X2
mat2X2=np.array([[1,2],[3,4]])
mat3X3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat2X2)
print(mat3X3)
matsec2X2=([[1,2],[3,4]])
reuslt=np.dot(mat2X2,matsec2X2)
print(reuslt)
#transpose 
transopse=np.transpose(mat3X3)
print(transopse)#can also you shape function
#inverse 
result=np.linalg.inv(mat2X2)
print(result)
#find determinant
det=np.linalg.det(mat3X3)
print(det)

#flatten Matrix in Numpy
mat3X3=np.array([[1,2,3],[4,5,6],[7,8,9]])

result=mat3X3.flatten()
print(result)
marr=np.array([1,2,3,4,5])
for x in marr:
    print(x)
print("\n")

for x in mat3X3:
    print(x)
print("\n")


for x in mat3X3:
   for y in x:
        print(y)
print("\n")

#excerise 3 continued
#Write a python program to find the sum of unit digit in the number
#of the given list l2 = [25, 36] output: 11

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

# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
l1=(8, 2, 3, -1, 7)
multiply=1
for i in l1:
    multiply=i*multiply
print("multipication of l1:-",multiply)
# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
something="1234abcd"
print(reversed(something))
# Write a Python function to calculate the factorial of a number (a non-negative integer). The function
# accepts the number as an argument
def factorialCalculator(num):
    factoial=1
    for i in range(1,num+1):
        factoial*=i
    return factoial
num=5
value=factorialCalculator(num)
print(value)
# Q.1 Write a Python program to find missing numbers from a list.
# Input: [1,2,5,10,11,14,17,20]
# Output: [3,4,6,7,8,9,12,13,15,16,18,19]
list2 = [1,4,5,6,7,9,14,17,20]
listmis = [] 

for i in range(1,len(list2)) :
    for j in range(list2[i-1]+1,list2[i]) :
        listmis.append(j)
print(listmis)

# Write a Python program to check a sequence of numbers is an arithmetic progression or not.
# Input: [1,8,27,64] [1,3,7,2]
# Output: True False


# Write a python program to check whether the given numbers in list is palindrome or not. If
# palindrome then check number in list is prime or not.
# Input: [121,132,454,111,147
l12= [121,132,454,111,147]
countflag=0
for i in l12:
    if l12[i]==l12[::-1]:
        for j in np.sqrt(i):
            if(num%i==0):
                countflag+=1

            if(countflag==0):
                print("number ",num," is prime ")
            else:
                print("number ",num," is not prime ")
