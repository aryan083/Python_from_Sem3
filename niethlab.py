import numpy as np

#to get the dimantion of a given array
a=np.array(65)
b=np.array([1,2,3,4])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
e=np.array([[[1,2,3],[4,5,6],[7,8,9]]
            ,[[1,2,3],[4,5,6],[7,8,9]],
            [[1,2,3],[4,5,6],[7,8,9]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
#to get the data type of a array it depands on which data type 
# of higest value is prensent in the array  it will give the size of the
# higest data tye to all the element of array
#i.e. sum of all the data type size of elements 
c=np.array([[1,2,3],[4,5,6]])
print(c.itemsize)
print(c.dtype)

c=np.array([[1,2.542424,3],[4,5.5424232,6]])
print(c.itemsize)
print(c.dtype)

c=np.array([[1,2,+23-3j],[4,5,6+6j]])
print(c.itemsize)
print(c.dtype)

c=np.array([[1,'2','3'],['4','5',6]])
print(c.itemsize)
print(c.dtype)

c=np.array([["AR","YA","N"],["4",5,6]])
print(c.itemsize)
print(c.dtype)

random=np.random.rand(4,8)
print(random)
#to get the mean of a row 
c=np.array([[1,2,3],[4,5,6]])
print(np.mean(c,axis=0))
print(np.mean(c,axis=1))
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[4,5,6],[1,2,3]])
e=np.append(c,d)
print(e)

c=np.array([[1,2],[3,4],[5,6]])

# print(np.insert(a,2,[4,5],axis=0))
# print("\n")
# print(np.insert(a,2,[5,4],axis=1))
# print("\n")
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)
print(np.add(x,y))
print("\n")
print(x-y)
print(np.subtract(x,y))
print(x*y)
print(np.multiply(x,y))
print(x/y)
print(np.divide(x,y))
print(np.multiply(x,y))
print(np.dot(x,y))
print(np.cross(x,y))
x=np.array([[1,2,3]],dtype=np.float64)
y=np.array([[[4],[5],[6]]],dtype=np.float64)

sum=x+y

print(sum)



















