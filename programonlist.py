
 
 
'''           
3) Hpw to use zip() function in list?

lst1_name =['Nikki', 'himani', 'abc', 'sam']
lst2_field=['comp', 'it', 'electronics', 'comp']
lst3_rollno=[21, 22, 23, 24]

lstzip = zip(lst1_name, lst2_field, lst3_rollno)
for lst1_name,lst2_field,lst3_rollno in lstzip:
    print("My name is %s my field is %s my roll number is %s " %(lst1_name, lst2_field, lst3_rollno))

op:
My name is Nikki my field is comp my roll number is 21 
My name is himani my field is it my roll number is 22 
My name is abc my field is electronics my roll number is 23
My name is sam my field is comp my roll number is 24
'''        

'''    
4) difference between append and extend in list
appned: the append method add item to the end of the list

num1=[2, 3, 4, 5, 6]
num2=[2,3,4]
num1.append(num2)
print(num1)

op:
[2, 3, 4, 5, 6, [2, 3, 4]]

extend : the extend() method will the extend list by appending all values in the list 

num1=[2, 3, 4, 5, 6]
num2=[2,3,4]
num1.extend(num2)
print(num1)

op:
    [2, 3, 4, 5, 6, 2, 3, 4]
'''


'''
 difference between del and clear
del: del() used to remove an item from list according to index number

lst=[2,3,4,5,6]
del lst[3]
print(lst)

clear: clear() method will clear all the elemets from the list

lst=[2,3,4,5,6]
lst.clear()
print(lst)

op:
    [] empty list
'''

'''
5) access element of the list 

lst=[2,3,4,5,6,7,8]
for i in lst:
    print(i)
    
op:
2
3
4
5
6
7
8
'''


'''
# how to concatenate two list 

num1=[1,2,3,4,5]
num2=[4,5,6,7,8]
print(num1+num2)

op:
[1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
'''

'''
# how to repalce element of list 

num=[1,2]
num[0]= 22
print(num)

op:
[22, 2]
'''

'''
adding values of two list using zip() method

lst=[2,3,4,5,6]
lst2=[8,7,6,5,4]
lst3=[]
for i,j in zip(lst, lst2):
    lst3.append(i+j)
print(lst3)

op:
[7, 8, 9, 10, 11]
'''


'''
adding values of two list without using any function 

lst=[2,3,4,5,6]
lst2=[5,6,7,8,9]
lst3=[]
for i in range(0, len(lst)):
        lst3.append(lst[i]+lst2[i])
print(lst3)

op:
[7, 9, 11, 13, 15]
'''


'''
n=input("enter the first list")
a=n.split()
for i in range(0, len(a)):
    a[i]=int(a[i])
x=input("enter the first list")
b=x.split()
for i in range(0, len(b)):
    b[i]=int(b[i])
print(a)
print(b)
for i in a:
    for j in b:
        if i>=j:
            print("1",end='')
        else:
            print("0", end='')
    break

o/p:
enter the first list2 3 4 5
enter the first list3 4 5 6
[2, 3, 4, 5]
[3, 4, 5, 6]
0000
'''

'''
2)find the duplicate element and remove that duplicate elements from list
lst=[2,3,4,5,2,5]
lst2=[]
lst3=[]
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            lst2.append(lst[i])    
print(" duplicate elemnts are",lst2)
for i in lst:
    if i not in lst3:
        lst3.append(i)
print("No duplicate values",lst3)

op:
duplicate elemnts are [2, 5]
No duplicate values [2, 3, 4, 5] 
'''

'''
remove duplicate elements of list 

lst=[5,6,7,8,9,0,8,7,5,6]
lst2=set(lst)
print(list(lst2))

op:
[0, 5, 6, 7, 8, 9]
'''

'''
 occurance of elements in list 

lst=[5,7,8,9,0,5,4,32,5,6]
print(lst.count(5))

op:
3
'''

'''
how to faltten list in python 

lst=[[2,3,4],[4,4,6],[8,9,7]]
lst2=[]
for i in lst:
    for j in i:
        lst2.append(j)
print(lst2)

op:
    [2, 3, 4, 4, 4, 6, 8, 9, 7]
'''


'''
coverting list in dictionary

lst=[(2,3),(4,5),(6,7)]
lst2= dict(lst)
print(lst2)

op:
  {2: 3, 4: 5, 6: 7}  
'''

'''
square value of all elements inside list 

lst=[2,3,4,5,6]
lst2=[]
for i in lst:
    lst2.append(i*i)
print(lst2)

op:
[4, 9, 16, 25, 36]
'''





