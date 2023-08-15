import numpy as np
#1 create a 3X3 Matrix with value from 2 to 10
mat3X3=np.array([[2,3,4],[5,6,7],[8,9,10]])
print(mat3X3)

#Write a numpy program to create a null vector of size 10 and update sixth value to 11
index=int(input("Enter a number from 0 to 9")) 
vect=np.zeros([10])
print(vect)
vect[index]=11
print(vect)
# Write a numpy code to create an 4X4 matrix and fill it with a checkboard pattern
mat4X4=np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
print(mat4X4)

arrat=[1,2,3,4,2,2,3,4]
max(arrat)
min(arrat)
print(max(arrat),min(arrat))
mat3X3=np.array([[2,3,4],[5,6,7],[8,9,10]])
pri=list(arrat)
max(set(pri),key=pri.count)
print(max(set(pri),key=pri.count))
#content 

arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
arr1=np.array([[1,2],[3,4]])
for i in np.nditer(arr):
    print(i)
print("\n")
# newarr=np.array_split(arr,3)
# print(newarr)
# print("\n")

#seaching in array

arrat=np.array([1,2,3,4,2,2,3,4])
x=np.where(arrat==4)
print(x)
print("\n")
#sorting a array
arrat=([1,2,3,4,5,6,3,53,2,12])
print(np.sort(arrat))
arrat=(["banana","mango","apple"])
print(np.sort(arrat))
print("\n")
array=np.array([[[1,2,3,4,5]],[[1,2,3,4,5]],[[1,2,3,4,5]],[[1,2,3,4,5]],[[1,2,3,4,5]]])
#opne a file 
file =open("array","wb")
np.save(file,array)
file.close
file =open("array","rb")
arra1=np.load(file)
print(arra1)
file.close()

#post alab
#How could you create a ten-eleemnt array of random int from 0 to 5 inclusve



