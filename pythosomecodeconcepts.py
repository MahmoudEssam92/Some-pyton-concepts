i = 1
while i <=10:
    print(i)
    i +=1
print('loop has finished')

################################################ -*- coding=utf-8 -*-
#the previous code shows the way that while loop is playing and it's role, when the compiler
#reach the while loop, it starts to do operations inside it: - first: he prints i then he finds 
#that condition ( i +=1 ) so he increases i with one and return to the first condition in while loop 
#to repeat it again till the result exceeds the limit ( i <=10) #
i = 1
while i <=10:
    i += 1
    if i == 6:
        continue
    print(i)
    
print('loop has finished')
# Using the continue statement above - in the while loop - makes it skip printing if i == 6, and continue the loop
#####################################################

Mahmoud = "Ahmed Essam"
for letter in (Mahmoud):
    print(letter)
    
    
friends = ["Yahia", "Omar", "Ahmed"]
for friend in friends:
    print(friend)
    
#
# in the above code, showing the role of for loop which is used to print every char or letter or name in lists
# or in a string 
# #

for x in range(10):
    print(x)
Hello = ["Ali", "Ahmed", "Mohamed", "Menna"]
for x in range(len(Hello)):
    print(x)

#in the previous, the for loop wil print the range till 9 not including 10 
#also the second one shows that we can use functions inside range in the for loop as it we can use it to know and count
#the number of names or characters in a list or string

for index in range(10):
    if index % 2 == 0:
        print(index, "number is even")
    else:
        print(index, "number is odd")

#################################################################################

text = "Mahmoud Essam is member at Huawei ITB Elites"
job_title = " Huawei Certified ICT Associate Artificial Intelligence "
print(text.upper())                                      # makes all chars in text in upper case
print(text.lower())                                      # makes all chars in text in lower case
print(text[0])                                           # print the first char or letter or string in a list or a sentence stored in a variable
print(text[0], job_title[5])                             # find the number of index in a string or list and then print it out
print(job_title.replace("Huawei", "Google"))             # to replace a string or a word with another which stored in a variable

## -*- coding=utf-8 -*-#####################################################

name = input("enter your name: ")                   # We use the input to read an input from user and do some operations on it
job_title = input("enter your position :")
print("hello" + name + job_title)

############## # -*- coding=utf-8 -*-

List_1 = ["hotaa", "Ota", "Conan", "Eren", "Leavi"]
List_2 = List_1.copy()             # This function copy the list1 to list2 but any changes made on list_1 don't appear in the list2
List_1.append("soso")              # Use .append To add a data such as names, strings, boleans, numbs to a list. It adds it at the end of the list
List_1.insert(1, "molan")          # Use .insert To add a any kind of data to a list with identifying its position on the list
List_1. remove("soso")             # Use .remove to delete any kind of data from a list
List_1.clear()                     # Remove all 
List_1.sort()                      # Sort the list    
print(List_1)

# -*- coding=utf-8 -*-############### -*- coding=utf-8 -*-

Coordinates = (5, 6)                                 # This is Tuples, Note that it's different of lists as we can not modify any data on the tuples
List_of_Tuples = [(5, 4), (5, 3), (5, 2), (5, 1)]    # We can also make a list of tuples which is unmodified too   
print(Coordinates[0])

############################## # -*- coding=utf-8 -*-

def say_hi(name, age):
    print("Hello" + name + ": " + age)
    
# NOTE, The function will not work until you call it 
say_hi(Mahmoud, "20")       # that is the right way to call the function and make it work 

def cube(number):
    return number*number*number         
# We use cube to find the power ^3. and we use return to make the calculation occur, Because without it, It doesn't work.
print(cube(5))
 
 ####################################3 # -*- coding=utf-8 -*-
 
def max_num(num1, num2, num3):              # To compare 2 numbers
     if num1 >= num2 and num3 >= num3:
         return num1
     elif num2 >= num1 and num2 >= num3:
         return num2
     else:
         return num3
print(max_num(5,8,3))
print(max_num(5,33,100))

###################################### ### -*- coding=utf-8 -*-

convert_month = {
                                        # This is a dictionary. To identify a dictionary we use {} and put values inside it 
    "jan" : "January",
    "feb" : "February",
    "mar" : "March"
    
}
print(convert_month.get("jan"))         # To call a value from the dictionary
print(convert_month["mar"])             # To call a value from the dictionary

##################################################### ## -*- coding=utf-8 -*-

def Great_Friends(F):
    for x in F:
        print("hi" + x)
Great_Friends(["Ahmed", "Ali", "Mohammed", "Taha"])

########################################################### ##
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.edex("@" + old_domain)
        new_emai = email[:index] + "@" + new_domain
        return new_emai
    return email
##################################################### ## -*- coding=utf-8 -*-
x = " Mahmoud Essam Mahmoud Salm"
print(x.split())       # Split function is used to cebarate a string sentence to make it as a list

helloeo = "HTML CSS Python Java"
print(helloeo.replace("Java", "JS"))       # Replace function, can be used to replace chars or words in a sentence with anotherone