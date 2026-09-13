#name = "Alex"
#age =34
#is_learning = True
#print(name)
#print("My age is", age)

#def add(a,b):
 #  return a+b
#print(add(3,7))

#1.Create a variable with your name and a variable with your years of Power Platform experience. Print a sentence combining both, e.g. "Alex has 6 years of Power Platform experience."
#name ="AJ"
#experiance = 6
#print(name," Has ",experiance ," Years of experiance in microsoft Power platform development")

#AJ  Has  6  Years of experiance in microsoft Power platform development

#2. Create two number variables and print their sum, difference, product, and division.
#number1 = int(input("Eneter first number: "))
#number2 = int(input("Eneter second number: "))
#addition function 
#def add(a,b):
 #   return a+b
#def sub(a,b):
 #   return a-b;
#def mul(a,b):
 #   return a*b
#def div(a,b):
 #   return a/b
#def floordiv(a,b):
 #   return a//b
#def moddiv(a,b):
 #   return a%b
#print("Addition of first two numbers",add(number1,number2))
#print("Subtraction of first two numbers",sub(number1,number2))
#print("Multiply of first two numbers",mul(number1,number2))
#print("Division of first two numbers",div(number1,number2))
#print("Floor Division of first two numbers",floordiv(number1,number2))
#print("Modulo Division of first two numbers",moddiv(number1,number2))
#Eneter first number: 55
#Eneter second number: 77
#Addition of first two numbers 132
#Subtraction of first two numbers -22
#Multiply of first two numbers 4235
#Division of first two numbers 0.7142857142857143
#Floor Division of first two numbers 0
#Modulo Division of first two numbers 55

#3.Create a list of 5 Microsoft products you've worked with. Print the whole list, then print just the first and last item.

#list_of_courses =[]
#print("Enter elements type done to stop")
#while True:
 #   user_input =input("Enter an item: ")
 #   if user_input.lower() == 'done' :
 #       break
 #   list_of_courses.append(user_input)
#print("Here are the courses list ",list_of_courses)
#print("Here is the first item",list_of_courses[0])
#print("Here is the last item",list_of_courses[-1])
#Enter elements type done to stop
#Enter an item: Power automate
#Enter an item: Power apps
#Enter an item: Power BI
#Enter an item: AI Builder
#Enter an item: Copilot studio
#Enter an item: done
#Here are the courses list  ['Power automate', 'Power apps', 'Power BI', 'AI Builder', 'Copilot studio']
#Here is the first item Power automate
#Here is the last item Copilot studio

#4. Add a 6th product to that list using .append(), then remove the 2nd one using .remove(). Print the list after each change.

#list_of_courses =[]
#print("Enter elements type done to stop")
#while True:
#    user_input =input("Enter an item: ")
 #   if user_input.lower() == 'done' :
 #       break
  #  list_of_courses.append(user_input)
#list_of_courses.append("Dataverse")
#list_of_courses.remove("AI Builder")
#print("Here are the courses list ",list_of_courses)
#Enter elements type done to stop
#Enter an item: PowerApps
#Enter an item: Power Automate
#Enter an item: AI Builder
#Enter an item: Copilot Studio
#Enter an item: PowerBI
#Enter an item: done 
#Here are the courses list  ['PowerApps', 'Power Automate', 'Copilot Studio', 'PowerBI', 'Dataverse']

#Create a dictionary representing yourself with keys name, role, years_experience, skills (where skills is a list). Print each value individually.

#keys =[]
#print("Enter keys once completed enter done")
#while True:
#    key_input = input("Enter Key: ")
 #   if key_input.lower()=='done':
  #      break
   # keys.append(key_input)
#my_dict = {}
#for key in keys:
 #   my_dict[key]=[]
  #  print(f"\nEntering vlaues for '{key}' (type 'done' to finish the key ")
 #  # while True:
    #    key_value=input(f"\nEnter Values for the '{key}': ")
     #   if key_value.lower() == 'done':
      #      break
       # my_dict[key].append(key_value)
#print("Here is the final dicitionary",my_dict)

#my_dict = {
 #   "Name": "AJ",
  #  "Role": "AI Engineer",
   # "Years of Experiance ": 6,
    #"skills": ["Power Apps","Power Automate","Power Bi","Copilot Studio","AI Builder"]

#}
#print("f/nHere is my list",my_dict)
#for key in my_dict:
 #   print(f"\n",key,": value :",my_dict[key])
  
 #Name : value : AJ

 #Role : value : AI Engineer

 #Years of Experiance  : value : 6

 #skills : value : ['Power Apps', 'Power Automate', 'Power Bi', 'Copilot Studio', 'AI Builder']

#Write a for loop that prints every item in your skills list with the word "Skill:" in front of each one.

#my_dict = {
 #   "Name": "AJ",
  #  "Role": "AI Engineer",
   #"Years of Experiance ": 6,
  #"skills": ["Power Apps","Power Automate","Power Bi","Copilot Studio","AI Builder"]

#}

#for skill in my_dict["skills"]:
 #      print(f"\n",skill)

#Power Apps

 #Power Automate

 #Power Bi

 #Copilot Studio

 #AI Builder

#7. Write a while loop that counts from 1 to n and prints each number.

#n = int(input("Enter the maximum number in range"))
#i=1
#while i <n+1:
#    print(i)
#    i+=1
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

#list1= [4, 8, 15, 16, 23, 42]
#for num in list1:
  #  if(num%2==0):
   #     print(num)
#4
#8
#16
#42

#9.Write a function square(n) that returns n * n. Call it with 3 different numbers and print each result.

#def square(n):
#    return n*n
#print(square(7))
#print(square(17))
#print(square(72))
#49
#289
#5184

#10.Write a function is_even(n) that returns True if a number is even, False if odd. Test it on 4 numbers.

#def is_even(n):
#    if(n%2==0):
#       return True
#print(is_even(18))
#print(is_even(17))
#print(is_even(34))
#True
#None
#True

#11.Write a function total_experience(list_of_years) that takes a list of numbers (years of experience per project) and returns their sum using a loop.
#def total_experience(list_of_years):
#    sum=0
#    for i in list_of_years:
#        sum+=i
#    print(sum)
#list_of_years =[7,11,23,2,1]
#total_experience(list_of_years)
#44
#12.Combine a dictionary and a loop: create a dictionary of 3 people ({"name": years} pairs) and loop through it printing "NAME has YEARS years of experience" for each.
#my_dict ={
 #   "Name":["AJ","Vishnu","Bhanu"],
  #  "Years":[6,4,7]
#}
#for name,year in zip(my_dict["Name"],my_dict["Years"]):
 #       print(name," Has ",year,"of Experiance")
#AJ  Has  6 of Experiance
#Vishnu  Has  4 of Experiance
#Bhanu  Has  7 of Experiance
 
#13.Write a function classify_level(years) that returns "Junior" if years < 3, "Mid" if 3–7, "Senior" if > 7 (use if / elif / else).
#def  classification(yoe):
#    if(yoe<3):
 #       return "Junior"
 #   elif( yoe>3 and yoe<7):
 #       return "Mid"
#  else:
##        return "Senior"
#n= int(input("Enter a number: "))
#print(classification(n))
#Senior

#14.Combine everything: create a list of 3 dictionaries, each representing a person (name, years_experience). Loop through the list, and for each person, call classify_level() and print "NAME is a LEVEL".
#def  classification(yoe):
 #   if(yoe<3):
  #     return "Junior"
   # elif( yoe>2 and yoe<7):
    #    return "Mid"
    #else:
     #  return "Senior"

#my_dict={
#    "Name":["AJ","Vishnu","Bhanu"],
#    "YOE":[2,3,9]
#}
#for name,yoe in zip(my_dict["Name"],my_dict["YOE"]):
#    classifylevel = classification(yoe)
#    print(name,"is belongs to",classifylevel,"Level")

#15.Bonus/stretch: write a function average(numbers) that takes a list of numbers and returns the average (sum divided by count — use len()).

num = []
while True:
    user_input= input("Enter numbers to the list once complete please Enter 'done' ")
    if(user_input == "done"):
        break
    num.append(int(user_input))
l=len(num)
sum =0;
for i in num:
    sum+=i
print("here is the avarage of the list",sum/l)

Enter numbers to the list once complete please Enter 'done' 5
Enter numbers to the list once complete please Enter 'done' 7
Enter numbers to the list once complete please Enter 'done' 22
Enter numbers to the list once complete please Enter 'done' 33
Enter numbers to the list once complete please Enter 'done' done
here is the avarage of the list 16.75
PS C:\Users\ajavi\NBL\ai-architect-90-day-journey> 