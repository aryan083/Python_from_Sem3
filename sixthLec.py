#task 1 use for loop task 1  
str= "Aryan Mahida"

for i in str: #Taks2
    print(i ,end ="")

for i in str:   #task3
    print(i,end="*")

#Task print the elements of list with help of for loop task 4
print()
l1={1,2,3,4,5,6}
for i in l1:
    print(i)

# task 3 after first darft find the average of numbers in a list usign loop task 5

sum=0;
lengthofl1=len(l1)
for i in l1:
    sum=i+sum;
print(sum)
print((sum/lengthofl1))

#for loop using tuuple
tup=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in tup:
    print(i)
    sum+=i;
print(sum/len(tup))

#Task 4 for loop using the range function task 6

for i in range(0,11):
    print(i)
# Task  8 Write a python code for calculating the factorial of given number

number =int(input("Enter a number to find its factorial "))
factorial=1;
for i in range(1,number+1):
    factorial*=i;

print(factorial)


#task 8 Create a table
number= int(input("Enter a number to get its table"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)

#task 9 for loop usign range len function

list2= ["C++","C","JAVA","C#","Python",]
for i in range(len(list2)):
    print("Hello",list2[i]);

for i in range(len(list2)):
    print("Hello",list2[i]);

#task10 nasted for loop
list3=["Google","Amazon","Microsoft","Meta","Tesla","Apple","AMD","intel","nVedia"]
for i in list2:
    print("EACH",i)
    for j in list3:
        print(j)

#Task 11 for loop with else close function
for i in range(0,10):
    print(i)
else:
    print("the loop is ended")

#task 12 for loop with break statement

for i in range(0,12):
   # print(i)
    if i==11:
        break;
    else :
        print(i)
#task 123 for loop with continue statment 

for i in range(0,12):
   # print(i)
    if i==6:
        continue;
    else :
        print(i)


#lab file tasks
# Task  8 Write a python code for calculating the factorial of given number

number =int(input("Enter a number to find its factorial "))
factorial=1;
for i in range(1,number+1):
    factorial*=i;

print(factorial)

#Task append that appends the square of each number in new list
list1=[2,4,8,9]
list2=[]
for i in list1:
    list2.append(i**2)
print(list2)
#Task append that filters the positive  and neagative number from a list
listnum=[1,2,3,4,5,6,7,8,9,-10,-12,-13,-11,-14,15,-16,17]
negative=[]
pos=[]
for i in listnum:
    if i<=0:
        pos.append(i)
    else:
        negative.append(i)
print(negative,"\n",pos)

#Task append that filters the even and odd number from a list

listnum=[1,2,3,4,5,6,7,8,9,10,12,13,11,14,15,16,17]
even=[]
odd=[]
for i in listnum:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd,"\n",even)

# task print all even numbers in given range

listalleven=[]
number=int(input("Enter a number "))
for i in range(0,number+1):
    if (i%2==0):
        listalleven.append(i)

print(listalleven)

#task to calculate sum of all number till given range

number = int(input("enter a number to find its sum"))
sum=0;
for i in range(0,number+1):
    sum+=i;
print(sum)

#task to  calculate the sum of all odd numbers in given range

number = int(input("enter a number to find its sum"))
sum=0;
for i in range(0,number+1):
    if( i%2!=0):
        sum+=i;
print(sum)
#task to calculate the table of number
number= int(input("Enter a number to get its table"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)

#task to calcualte the total digits in given number

number= (input("Enter a number to get its table"))
print(len(number))

#task to check if given strign is pendrome or not


str= (input("Enter a string to get its table"))
if (str==reversed(str)):
    print("given string is pelindrome")
else:
    print("given string is pelindrome")

#task to find number of digits and chars in a string enterd by user
str=input("Enter a string ")
charcount=0;
digitcout=0;
for i in str:
    if i.isdigit()==True:
        digitcout=digitcout+1
    else:
        charcount=charcount+1
print(charcount,digitcout)



#pettern print
N = int(input("Enter a number"));
  

for i in range(N):
  
        for j in range(0, i + 1):
            print("*", end = "")
        print()
  
    # Loop to print the lower half
    # diamond pattern
for i in range(1, N):
  
        for j in range(i, N):
            print("*", end = "")
        print()
  

