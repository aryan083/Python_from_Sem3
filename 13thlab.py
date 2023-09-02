import numpy as np
# pre lab
#1 To check wheater a specified value are presinet in a numpy array

nuparr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(4 in nuparr)

#2 Find the frequent value in numpy in a numpy array

pri=np.array([1,2,3,4,5,6,6,7,6,75,5])
print(max(set(pri),key=list(pri).count))
print("\n")

#3 Reverse a numpy array

revnp=()
nuparr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(list(nuparr[::-1,::-1]))
revsed =list(nuparr[::-1,::-1])

print(np.array(revsed))    

arr=np.identity(3)
arr2=np.tri
print(arr2)

#LAB STUFF

# file = np.loadtxt("fiirst.txt",dtype="str")
# print(file)
# print("\n")

# file = np.loadtxt("fiirst.txt",skiprows=1,dtype="str",)
# print(file)
# print("\n")
# F4=np.loadtxt("fiirst.txt",usecols=0,skiprows=1,dtype="str")
# print("\n",F4)
# for i in F4:
#     print(i)
# print("\n")

# F4=np.genfromtxt("fiirst.txt",dtype="str",delimiter=",")
# print("\n",F4)

# F5=np.genfromtxt("fiirst.txt",dtype="str",encoding=None,skip_footer=1)
# print(F5)

#post lab

#1 Obtating Boolean mat from binary mat

arr=np.array([1,0,1,0])

boolarr=np.array([])
for i in range(0,len(arr),1):
    if arr[i]==0:
        boolarr
    else:
        np.append(boolarr,False,0)
#2 getting the index 2 arrays which elent are same on the same index
arr=np.array([1,2,3,4,5,6,7])
arr2=np.array([1,2,4,43,5,6])
arrindex=np.array([])

for i in range(0,len(arr)):
    if(arr[i]==arr2[i]):
        np.append(arrindex,i,0)

print(arrindex)

#3  Array Generation by repeation of a small array across each dimension


