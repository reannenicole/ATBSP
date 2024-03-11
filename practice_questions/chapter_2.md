# 1. What are the two values of the Boolean data type? How do you write them?
the two Boolean operators types are True and False. They must be written with the capitals. 

# 2. What are the three Boolean operators?
and, or, not

# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

True and True = True
False and False = False
True and False = False
False and True = False

True or True = True 
False or False = False
True or False = True
False or True - True

not True = False
not False = True 

# 4. What do the following expressions evaluate to?
 (5 > 4) and (3 == 5)                   = False
 not (5 > 4)                            = False
 (5 > 4) or (3 == 5)                    = True
 not ((5 > 4) or (3 == 5))              = False
 (True and True) and (True == False)    = False
 (not False) or (not True)              = True

# 5. What are the six comparison operators?
==, !=, <, >, >=, <= 

# 6. What is the difference between the equal to operator and the assignment operator?
the equal to operator is written as == and compares two points of data, evaluating them down to a True or False Boolean expression (it is either equal or it isnt)
wheras the assignment operator is written as = and is used to assign data to a variable 

# 7. Explain what a condition is and where you would use one. 
A condition is the part of a flow statement that is being evaluated within the clause block. 

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = int(input("please write 1 or 2 "))
if spam == 1:
 print("Hello")
elif spam == 2: 
 print("Howdy")
else:
 print("Greetings")

# 10. What can you press if your program is stuck in an infinite loop?
ctrl+z or f5

# 11. What is the difference between break and continue?
break stops the programme wheras continue loops back to the start

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
each of these does the same thing, counting up from zero, increasing the integer by one each time until it hits 10 

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1, 11):
 print(i)

i = 1
while i <= 10:
  print(i)
  i = i + 1

# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()