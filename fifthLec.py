list1 = [1,2,3,4,5,(1,2,3,4,5)]
#print(list1([5][2]))
#print(list1([5[2]]))
tup1=(1,3,'5',[6,'7',8,True],8)
print(tup1[3][1])
str={ "a":"b","c":{"j","i","k","l"},"d":5}
print(str["c"])
fruit={"Apple": "Sasta","Mango": "Don't like","Banana":"Not Good"}
fruit1={"Orange":"Tasty","List":"Not Good"}
fruit.update(fruit1)
print(fruit)
fruit.pop("Apple")
print(fruit)
Set1={ 1,1,2,3,4,5,6,7}
print(Set1)
Set1.add(8)
print(Set1)
Set1.update([9,10],[11,12],[13,15])
print(Set1)
Set2={1,1,2,3,4,5,6,7,16,18,20,200}
print(Set1.intersection(Set2))
print(0o10)
print(0x10)
print(0b10)
print(oct(10))
print(hex(10))

print(bin(10))
tup1=("A","R","Y","A","N")#Needs the string only.
print(''.join(tup1))
# x=int(input("Enter a nnumber "))
# y=int(input("Enter second number"))
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**2)
# print(x+y*2)
# print(x>7 and x<7)
# print(x>7 or x<7)
# print(not(y>5))
# print(x is y)
# print(x is not y)
# print(x in y)
# print(x not in y)
tupple1=(11,22)
tupple2=(88,99)
print(tupple1)
print(tupple2)
tupple3=tupple1
tupple1=tupple2
tupple2=tupple3
print(tupple1)
print(tupple2)

tupple4=("MONKEY D. LUFFY",[10,20,30],15)
print(tupple4[1][1])

tup5=(11,[22,33],44,55)

tup5[1][0]=222
tup5[1][1]=333
print(tup5)
print("   *    "+"\n"+ "  *  *  "+"\n"+"***    ***")
x=56
if x>5:
    print("TRUE")
elif  x>50:
    print( "true")
else:
    print("False")
x=5
print(x)


