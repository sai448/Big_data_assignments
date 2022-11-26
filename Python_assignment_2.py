# Q26. What is a string? How can we declare string in Python?
#  A string is a combination characters and string is immutable
# Q27. How can we access the string using its index?
#  By sclicing we can access string

# Q28. Write a code to get the desired output of the following
#string = "Big Data iNeuron"
# desired_output = "iNeuron"
#print(string[9:])

# Q29. Write a code to get the desired output of the following

#string = "Big Data iNeuron"
# desired_output = "norueNi"
#ans:
#print(string[-1:-8:-1])

# Q30. Resverse the string given in the above question.
#print(string[-1::-1])
# Q31. How can you delete entire string at once?

# Q32. What is escape sequence?
# An escape sequence is a backslash followed by character , used to enter illegal characters
# Q33. How can you print the below string?

# 'iNeuron's Big Data Course'
#print("'iNeuron's Big Data Course'")
# Q34. What is a list in Python?
# LIST is an sequential data type , it is an hetrogeneous it accepts all data types
# Q35. How can you create a list in Python?
#li=[]
# Q36. How can we access the elements in a list?
# by using index
# Q37. Write a code to access the word "iNeuron" from the given list.

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# print(lst[4][2])
# Q38. Take a list as an input from the user and find the length of the list.
# li=input().split(" ")
# print(len(li))
# Q39. Add the word "Big" in the 3rd index of the given list.

# lst = ["Welcome", "to", "Data", "course"]
# lst.insert(2,"Big")
# print(lst)

# Q40. What is a tuple? How is it different from list?
# in tuple we cannot change values
# Q41. How can you create a tuple in Python?
#tuple=()

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
# tuple=()
# tuple.add("sai")
# print(tuple)
# in tuple we cannot add element it is immutable

# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
# t1=(1,2,3)
# t2=(4,5,6)
# t3=t1+t2
# print(t3)

# Q44. Take a tuple as an input and print the count of elements in it.
# t=(1,2,3)
# print(len(t))

# Q45. What are sets in Python?
# sets are unordered and not allows duplicate values

# Q46. How can you create a set?
# s1= set()
# print(type(s1))

# Q47. Create a set and add "iNeuron" in your set.
# s1=set()
# s1.add("iNeuron")
# print(s1)

# Q48. Try to add multiple values using add() function.
# By using add() function we cannot add more than one value

# Q49. How is update() different from add()?
#We use add() method to add single value to a set. We use update() method to add sequence values to a set. Here Sequences are any iterables including list , tuple , string , dict etc.

# Q50. What is clear() in sets?
# it removes all elements in a set

# Q51. What is frozen set?
# frozen set method makes iteratable in to unchangeable

# Q52. How is frozen set different from set?

# Q53. What is union() in sets? Explain via code.
# s1={1,2}
# s2={3,4}
# s3=s1.union(s2)
# print(s3)

# Q54. What is intersection() in sets? Explain via code.
# s1={1,2}
# s2={2,4}
# s3=s1.intersection(s2)
# print(s3)

# Q55. What is dictionary ibn Python?
# Dictionary is mapping data type , contains key value pairs

# Q56. How is dictionary different from all other data structures.
# it is mapping data strcuture, contain key and value pairs

# Q57. How can we delare a dictionary in Python?
# d={}
# print(type(t))
# Q58. What will the output of the following?

# var = {}
# print(type(var))
# ans: Dictionary

# Q59. How can we add an element in a dictionary?
# Ans: dictionary_reference[key:value]

# Q60. Create a dictionary and access all the values in that dictionary.
# dic={"sai":1,"teja":2}
# for i,j in dic.items():
#     print(f"key is:{i}","value is:",j)

# Q61. Create a nested dictionary and access all the element in the inner dictionary.
# dic={"sai":1,"teja":2,"AP":{1:"a",2:"b"}}
# for i in dic.values():
#     print(i)

# Q62. What is the use of get() function?

# The get() method returns the value of the item with the specified key.

# Q63. What is the use of items() function?

# items() function returns the both keys and values

# Q64. What is the use of pop() function?

#The pop() method removes the element at the specified position .

# Q65. What is the use of popitems() function?
# The popitem() method removes the item that was last inserted into the dictionary .

# Q66. What is the use of keys() function?
# it return keys of a dictionary as a list

# Q67. What is the use of values() function?
# it return values of a dictionary as a list

# Q68. What are loops in Python?
# loops are used to do a repeated work with effortless

# Q69. How many type of loop are there in Python?
# For loop, while loop

# Q70. What is the difference between for and while loops?
# For is used  when we know number of iterations
# While is used  when we dont know number of iterations

# Q71. What is the use of continue statement?
# Continue skips the below code

# Q72. What is the use of break statement?
# break will terminate the loop

# Q73. What is the use of pass statement?
# Pass is just an empty code it wont perform anything

# Q74. What is the use of range() function?
# range is used to define the min and max values and increment values

# Q75. How can you loop over a dictionary?
# using for loop we can access keys and values in dictionary

# Coding problems
# Q76. Write a Python program to find the factorial of a given number.
def fact(n):
    if n>=1:
        return fact(n-1)*n
    else:
        return 1  

# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
p=100
t=34
r=12
print("simple interest is:",(p*t*r)/100)

# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
p=100
t=34
r=12
print("Compound interest is:",p(1+r/100)*t)

# Q79. Write a Python program to check if a number is prime or not.


# Q80. Write a Python program to check Armstrong Number.

# Q81. Write a Python program to find the n-th Fibonacci Number.

# Q82. Write a Python program to interchange the first and last element in a list.

# Q83. Write a Python program to swap two elements in a list.

# Q84. Write a Python program to find N largest element from a list.

# Q85. Write a Python program to find cumulative sum of a list.
list=[10,20,30,40,50]
new_list=[]
j=0
for i in range(0,len(list)):
	j+=list[i]
	new_list.append(j)
	
print(new_list)

# Q86. Write a Python program to check if a string is palindrome or not.
# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")


# Q87. Write a Python program to remove i'th element from a string.
str="welcome"
n=int(input("Enter the position: "))
print(str.replace(str[n],' '))

# Q88. Write a Python program to check if a substring is present in a given string.
str=" This is Lionel messi"
sub_str="messi"
if sub_str in str:
    print("yes")    
            
# Q89. Write a Python program to find words which are greater than given length k.
n="hello geeks for geeks is computer science portal"; l=4
s=n.split(" ")
l=list(filter(lambda x: (len(x)>l),s))
print(l)

# Q90. Write a Python program to extract unquire dictionary values.
d1={'apple': 1, 'bat': 2, 'cat': 3, 'dog': 1}
l=[]
for i in d1.values():
    l.append(i)
print(set(l))    

# Q91. Write a Python program to merge two dictionary.
d1={"apple":1,"bat":2}
d2={"cat":3,"dog":4}
d5 = {**d1, **d2}
print(d5)


# Q92. Write a Python program to convert a list of tuples into dictionary.

li = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
dic={i[0]:j[1] for i in li for j in li }
print(dic)
# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

list = [9, 5, 6]
li=[(i,i**3) for i in list]
print(li)

# Q94. Write a Python program to get all combinations of 2 tuples.

# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

# Q95. Write a Python program to sort a list of tuples by second item.

# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

# Q96. Write a python program to print below pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('')
# Q97. Write a python program to print below pattern.

#     *
#    **
#   ***
#  ****
# *****
rows = 5
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print('*', end=' ')
            num += 1
    print("")

# Q98. Write a python program to print below pattern.

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
size = 5
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")



# Q99. Write a python program to print below pattern.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

# Q100. Write a python program to print below pattern.

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
