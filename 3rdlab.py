#can change index for string formats 
#also can give precision value for floating point number
# also can assing the value for each format bracket like veriables 
x= '{} paython,{}'
print(x.format(" i can","understand"))

x= '{0} paython,{1}'
print(x.format(" i can","understand"))

x= '{1} paython,{0}'
print(x.format(" i can","understand"))

nostudy= (215/420)*100
x= "result={r:3.2f}%".format(r=nostudy)
print(x)

#DATA STRUCTURE 
#tuple can have index value 
thistup1 =(0,1,2,3,4)
print(thistup1)
print(type(thistup1))

thistup2 =(False,1,"edam's",3,1.2)
print(thistup2)

thistup3 =(True,1+4j,"apple",3,4.20)
print(thistup3)
print(thistup3+thistup2)

thistup4 =(0,1,2,3,4)
print(thistup4)

tup1=("A",253,1+4j,4+1j,6)
tup2=("A","B","C",7+4j)
tup3=tup1+tup2
print((tup3[2]), (tup3[3]),(tup3[8]))
#LIST
L1=[1,"A",2.5,3+14j,False]
L1[0]=True
L2=["BATCH",3.1415,True,5,"FALSE"]
print(L1+L2)
print(L1,type(L1))

L1=[1,"6",'7',3.143+14j]
tup1=(6,9.28,3+2j)

tupop=(tup1[2],L1[1],tup1[0],L1[2])
print(tupop)

#List can be appended  using lsit.append function and can be inserted by using list.insert(index,stuff)

L3= ["BAGLO","PLUTO","RUSSIAN" ,"NOOB"]
L3.append("NONE")
print(L3)

L3.insert(2,"KITKAT")
print(L3)

