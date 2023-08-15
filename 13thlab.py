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

nuparr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(list(nuparr[::-1,::-1]))

#LAB STUFF

#post lab