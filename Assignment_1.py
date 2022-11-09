# ## Assignment Part-1
# Q1. Why do we call Python as a general purpose and high-level programming language?
# ANS: Code is understandable and we write in english

# Q2. Why is Python called a dynamically typed language?
# Strong typing means that variables do have a type and that the type matters when performing operations on a variable. Dynamic typing means that the type of the variable is determined only during runtime .

# Q3. List some pros and cons of Python programming language?
# Ans: large community--pros
       #slower than compiled language---cons
       
# Q4. In what all domains can we use Python?
# Ans: WEB , app Development and data domains

# Q5. What are variable and how can we declare them?
# ANS: Variables are reference to the data stored in a location , it is like an address

# Q6. How can we take an input from the user in Python?

# a=input()

# Q7. What is the default datatype of the value that has been taken as an input using input() function?
# ANS: str

# Q8. What is type casting?
# Ans: Changng the data type of variable or data

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
# ans: Yes 
# names= input().split(" ")

# Q10. What are keywords?
# Keywords are some predefined and reserved words in python that have special meanings 

# Q11. Can we use keywords as a variable? Support your answer with reason.
# No , 

# Q12. What is indentation? What's the use of indentaion in Python?
# Ans: Indentation refers to the spaces at the beginning of a code line

# Q13. How can we throw some output in Python?
# Ans: with print function

# Q14. What are operators in Python?
# Ans: they are used to perform specific operations like addition,subtraction, etc.

# Q15. What is difference between / and // operators?
# ans: / is gives float output and // gives int output

# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# ```
print("iNeuroniNeuroniNeuroniNeuron")

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
number = int(input())
if number%2==0:
    print("even")
else:
    print("odd")    

# Q18. What are boolean operator?
# AND, OR, NOT

# Q19. What will the output of the following?
# ```
# 1 or 0-----> 1

# 0 and 0----->0

# True and False and True----->False

# 1 or 0 or 0---->1
# ```

# Q20. What are conditional statements in Python?
# if,else,elif

# Q21. What is use of 'if', 'elif' and 'else' keywords?
# used to write logic based on conditions

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age=int(input())
if age>18:
    print("I can vote")
else:
    print("I can't vote")    

# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        sum+=numbers[i]
print(sum)

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
x,y,z=input().split(",")
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)
    

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions

# - The number must be divisible by five

# - If the number is greater than 150, then skip it and move to the next number

# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(len(numbers)):
    if numbers[i]%5==0:
        if numbers[i]<=150:
            if numbers[i]<=500:
                print(numbers[i])
            else:
                break    