#1.Python program to Print Elements in a List
'''
li = [10,20,30,40]
for i in li:
    print(i)
'''

#2.Python Program to Print List Items in Reverse Order
'''
li = [10,20,30,40]
for i in li[::-1]:
    print(i)
'''

#3.Python Program to Print List Items Greater Than Average
'''
li = [10,20,30,40]
total = sum(li)
count = len(li)
avg = total / count
for i in li:
    if(i > avg):
        print(i)
'''

#4.Python Program to Print List Items at Even Position
'''
li = [10,20,30,40]
for i in range(len(li)):
    if(i%2==0):
        print(li[i])
'''

#5.Python Program to Print List Items at Odd Position
'''
li = [10,20,30,40]
for i in range(len(li)):
    if(i%2!=0):
        print(li[i])
'''

#6.Python Program to Print Even Numbers in a List
'''
li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    if(i%2==0):
        print(i)
'''

#7.Python program to Print Odd List Numbers
'''
li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    if(i%2!=0):
        print(i)
'''

#8.Python program to Put Even and odd Numbers in Separate List
'''
li = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in li:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even number :- ",even)
print("Odd NUmber :- ",odd)
'''

#9.Python program to Print Positive Numbers
'''
li = [1, 2, 3, -4, 5, -6, -7, 8, 9, 10]
for i in li:
    if(i>0):
        print(i)
'''

#10.Python program to Print Negative Numbers
'''
li = [1, 2, 3, -4, 5, -6, -7, 8, 9, 10]
for i in li:
    if(i<0):
        print(i)
'''

#11.Python program to Put Positive and Negative Numbers in Separate List
'''
li = [1, 2, 3, -4, 5, -6, -7, 8, 9, 10]
positive = []
negative = []
for i in li:
    if(i>0):
        positive.append(i)
    elif(i<0):
        negative.append(i)
print(positive)
print(negative)
'''

#12.Python program to Print the Largest Number in a List
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
high = li[0]
for i in range(len(li)):
    if(li[i] > high):
        high = li[i]
print("Largest number :- ",high)
'''

#13.Python program to Print the Second Largest Number in a List
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
li.sort(reverse=True)
print(li[1])
'''

#14.Python program to Print the Largest and Smallest Number
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
high = li[0]
small = li[0]
for i in range(len(li)):
    if(li[i] > high):
        high = li[i]
for i in range(len(li)):
    if(li[i] < small):
        small = li[i]
print("Largest number :- ",high)
print("Smallest number :- ",small)
'''

#15.Python program to Print the Smallest Element in a List
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
small = li[0]
for i in range(len(li)):
    if(li[i] < small):
        small = li[i]
print("Smallest :- ",small)
'''

#16.Python program to Remove Duplicates from List
'''
li = [10,20,30,10,10]
s1 = set(li)
print(list(s1))
'''

#17.Python program to Remove Even Numbers in a List
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
li = [i for i in li if(i%2!=0)]
print(li)
'''

#18.Python program to Reverse List Items
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
print(li)
li.reverse()
print(li)
'''

#19.Python program to Sort List Items in Ascending Order
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
print(li)
li.sort()
print(li)
'''

#20.Python Program to Sort List Items in Descending Order
'''
li = [1, 2, 3, -4, 5, 132, -6, -7, 8, 9, 10]
print(li)
li.sort(reverse=True)
print(li)
'''














































































































