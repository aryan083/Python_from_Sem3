# #while Loops 
# i=0
# while i<=10:
#     print(i)
#     i+=1
# print("\n")

# i=0
# while i<=10:
#     if i==5:
#         continue
#     print(i)

#     i+=1

# print("\n")
# i=0
# while i<=10:
#     if i==5:
#         break
#     print(i)

#     i+=1

# print("\n")
# i=0
# while i<=10:
#     if i==5:
#         pass
#     print(i)
#     i+=1

    # user defined function use def for function declation
def First_fun_By_ARyan():
    print("This  Is A First Function")

First_fun_By_ARyan()

def YourName(name):
    print(name)

YourName("Aryan Mahida")

#Scoping

def Scope():
    a=55
    print(a)
    print("\n")

a=100
Scope()
print(a)

#function with return value

def SquareCal(num):
    num=num**2
    return num

b=SquareCal(6)
print(b)

#nasted Function 
def Fun_Out():
    print("Doing Fun Out")
    def Fun_In():
        print("Doing Fun In")
    Fun_In()


Fun_Out()
#lambda
t=lambda x:x**3
print(t(5))
x=4
def cube(x):
    return x**3
print(cube(x))

#Task pattern print

num=int(input("enter a number "))
for i in range(num):
  
        for j in range(num):
            print("#",end="")
        print()

#Task print sum of 0 to 100 of all even and all odd

OddSum=0
EvenSum=0
for i in range(0,101):
    if i%2==0:
        EvenSum=EvenSum+i
    else:
        OddSum= OddSum+i
print("Sum of odd Number ",OddSum,"\n Sum of Even Number ",EvenSum)

#Task wwwwwrite loop for series 10,20,30,40,50...300
for i in range (10, 301,10):
    print(i)
    i=i+10

#task 4 while loop 105,98,91...,7
i=105
while i>6:
    print(i)
    i=i-7

#task 5 check a number is prime 
countflag=0
num=int(input("Enter number to be checked if it is prime or not"))
for i in range(1,num+1):
    if(num%i==0):
        countflag+=1

if(countflag==0):
    print("number ",num," is prime ")
else:
    print("number ",num," is prime ")

#Task 6 Reverse a number 
num=(input("Enter number"))
print(num[::-1])

#task 7 Binary to decimal convertion 
num=int(input("Enter a binary number "))
decimal, i = 0, 0
while(num > 0):
    dec = num % 10
    decimal = decimal + dec * pow(2, i)        
    binary = num//10
    i += 1

print(decimal)


#task 8 check if number is  pelindrome
num=(input("Enter number"))
if(num==reversed(num)):
    print("given number is pelindrome")
else:
    print("given number is pelindrome")


