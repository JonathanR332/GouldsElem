from os import close
import random as ran 

print(2*2) # printing common math statements that they would know
print(2+2)
print(3-2)
print(3/2)
print(3**3)
print("Hello World") # printing text  

age = input("How old are you? ")
name = input("What is your name? ") #asking inputs for then to be displayed back 
score = 0

print("Hello, I am Mario" +"\nNice to meet you " + name + "\nIt is nice hearing you are " + age + " Years old. ")

print(ran.randint(0,100000)) #random number for fun


def my_quiz():
  print("Welcome to my quiz")
  score = 0
Answer = input("What Color is the sky? ")
if Answer == "Blue" or Answer == "blue": # intro to if statements however they could go avoiding it
  print("Correct")
  score  += 1 # score going up; introduction to operations.
  print("Your score is " + str(score))
else:
  print("Incorrect")
  print("Your score is " + str(score))  # display score and feedback

Answer2 = input("What color is grass? ")
if Answer2 == "Green" or Answer2 == "green":
  print("Correct")
  score += 1
  print("Your score is " + str(score))
else:
  print("Incorrect")
  print("Your score is " + str(score)) 

Answer3 = input("What color is Spongebob? ")
if Answer3 == "Yellow" or Answer3 == "yellow":
    print("Correct")
    score += 1
    print("Your score is " + str(score)) 
else:
  print("Incorrect")
  print("Your score is " + str(score)) 


print("The end: \n Thank you for playing " + name + " You got " + str(score) + " out of 3") # Final message to show users their score.





#Example output

# 4
#4
#1
#1.5
#27
#Hello World
#How old are you? 21
#What is your name? Alice
#Hello, I am Mario
#Nice to meet you Alice
#It is nice hearing you are 21 Years old.
#36862
#What Color is the sky? Blue
#Correct
#Your score is 1
#What color is grass? Green
#Correct
#Your score is 2
#What color is Spongebob? Yellow
#Correct
#Your score is 3
#The end:
#Thank you for playing Alice You got 3 out of 3

