Q1. What is the purpose of Python's OOP?
To solve the complex problem in a easier way and reduce the code lines

Q2. Where does an inheritance search look for an attribute?
---> An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, then in all higher superclasses, progressing from left to right (by default) . The search stops at the first place the attribute is found.

Q3. How do you distinguish between a class object and an instance object?
---> A class is an blueprint ,whereas object is an physical entity

Q4. What makes the first argument in a class’s method function special?
---> it is not an parameter it is an object reference

Q5. What is the purpose of the init method?
It is used to assign values to instance variables

Q6. What is the process for creating a class instance?
-->To do the various task based on methods  by inistiating the class and to make real world object occupies memory
ObjectName = ClassName()

Q7. What is the process for creating a class?
--> Class ClassName:

Q8. How would you define the superclasses of a class?
--> class ClassName(ParentClassName):

Q9. What is the relationship between classes and modules?
---> module is a file that is executable and  that contains set of classes and functions

Q10. How do you make instances and classes?
--> instances are maked with the help of class
obj = ClassName()
---> Class can be  defined as Class ClassName:

Q11. Where and how should be class attributes created?
--> When we want a variable constant for all the objects like Eg: college
By assigning value at the time of declaration

Q12. Where and how are instance attributes created?
---> At the time of creation of object ,instance variables get  initialized

Q13. What does the term "self" in a Python class mean?
---> It is used for object reference

Q14. How does a Python class handle operator overloading?
-->In Python implicitly handles overloading such that no need to multiple same methods eg: len()

Q15. When do you consider allowing operator overloading of your classes?
--> + is an example for operator overloading same implementation but different behaviour across int class and str class

Q16. What is the most popular form of operator overloading?
---> + sign

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Q18. Describe three applications for exception processing.
---> Zerodivisionerror, Index out of range, key not found


Q19. What happens if you don't do something extra to treat an exception?
---> Code execution will be terminated at the Exception

Q20. What are your options for recovering from an exception in your script?
---> try,except

Q21. Describe two methods for triggering exceptions in your script.
-->try,except

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of
whether or not an exception exists.
---> finally and else

Q23. What is the purpose of the try statement?
---> Most error prone code wriiten in try block and it is used handle exception and send the flow to except block

Q24. What are the two most popular try statement variations?
---> 1. try and Except
2.try except and else and Finally

Q25. What is the purpose of the raise statement?
---> raise is used to raise an exception

Q26. What does the assert statement do, and what other statement is it like?
---> assert statement is used to test a condition if the condition returns false then exception raised.

Q27. What is the purpose of the with/as argument, and what other statement is it like?
---> with statement is a replacement of try and finally block 
it performs same as try and finally

Q28. What are *args, **kwargs?
---> *args is a parameter to send multiple arguments
--->**kwargs is a parameter to send multiple key,value pairs

Q29. How can I pass optional or keyword parameters from one function to another?


Q30. What are Lambda Functions?
---> one line defination of function

Q31. Explain Inheritance in Python with an example?
---> Inheritance establish relation between parent class and child class 
Child class inherits the properties of parent class like methods and variables
class A:
    def speak(self):
        print("HI")
class B(A):
    pass
obj1 = B()
obj1.speak()

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?

Q33. Which methods/functions do we use to determine the type of instance and inheritance?


Q34.Explain the use of the 'The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

Q35. What is the global keyword?
---> global keyword will make the variable in to global variable it will be accessed anywhere in the code