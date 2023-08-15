tupp1=(1,2,3,4,5,(1,2,3,4,5))
list1 = [1,2,3,4,5,(1,2,3,4,5)]
tupp2=(6,7,8,9,10,(6,7,8,9,10))
list2 = [6,7,8,9,10,(6,7,8,9,10)]

print(tupp1[5]+tupp2[5])
print(list1[5]+list2[5])
tupp1=(1,2,3,4,5,[1,2,3,4,5])
list1 = [1,2,3,4,5,(1,2,3,4,5)]
tupp2=(6,7,8,9,10,(6,7,8,9,10))
list2 = [6,7,8,9,10,(6,7,8,9,10)]

#print(tupp1[5]+tupp2[5])
print(list1[5]+list2[5])

# pop will remove the last elemnt from list

print(list1.pop()) 

#remove function will remove the first occurance of element 

list2 = [6,'my',8,"nothing",10,(6,7,8,9,10)]

list2.remove('my')
print(list2)

#clear function willl clear the whole list 
list1.clear()
print(list1)

list1 = [1,2,3,4,5,(1,2,3,4,5)]
list2 = [6,'my',8,"nothing",10,(6,7,8,9,10),'my']

#count fun. will count the instance of each element 
list3 = [6,7,8,9,10,1,2,3,4,5]
print(list1.count((1,2,3,4,5)))

#reverse method will reverse the list
list2.reverse()
print(list2)
#sort inbuilt method for sorting
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
#task

tuppleori=(5,20,3,7,6,8)
listori= [5,20,3,7,6,8]


listori.sort()
print(listori)

tuplsecond= (2,4,5,6,2,3,4,4,7)
listsecond= (2,4,5,6,2,3,4,4,7)
print(tuplsecond.count(4))
print(tuplsecond.count(2))
print(tuplsecond.count(5))
print(tuplsecond.count(6))
print(tuplsecond.count(7))

dict_1={
        "a":"A",   
        "b":"B",   
        "c":"C",   
        "d":"D",   
        "e":"E",   
}
print(dict_1['e'])
print(dict_1.get('D'))

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
print(dict_1['a'])
#set 
myset= {1,2,3,2,42,4,6,3,521,4,1,"a"}
print(myset)
print(myset.add(1))
print(myset.)










