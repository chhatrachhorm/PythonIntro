import random
import sys
import os

print ("Hello World")
name = "Derek"
print (name)
# DataType
'''
Numbers
Strings
Lists
Tuples
Dictionaries
'''
print ("5 + 2 =" , 5 + 2)
print ("5 ** 2 =" , 5 ** 2)

print (5 // 2)

quote = "\nAlways remember that your are unique"
multiline_quote = '''
just
like
anyone'''
print ("%s %s %s" % ('I like the quote' , quote , multiline_quote))

print ("\n" * 5)
print ('I don\'t like new line' , end="")
print ("newlines")

# list

# one dimensional list
grocery_list = ['Juice' , 'Tomatoes' , 'Potatoes']
other_list = ['Going Home' , 'Eating Dinner']
# two dimensional list
todo_list = [grocery_list , other_list]
print ('First Item : ' , grocery_list[0])
print (grocery_list)
print (todo_list)
print (todo_list[1][0])
print (todo_list[1])
# dealing with list
grocery_list.append ('Onion')
grocery_list.insert (1 , 'Espresso')
grocery_list.remove ("Juice")
del other_list[1]
print (todo_list)

# combine lists together
todo_list2 = other_list + grocery_list
print (todo_list2)
print (len (todo_list2))
print (max (todo_list2))
print (min (todo_list2))

#  tuple -- unlike list because it cannot be changed after being created

pi_tuple = (1, 2, "Derek" , "Darson")
print (pi_tuple)
pi_list = list (pi_tuple)
print (pi_list)

re_pi_tuple = tuple (pi_list)
print (re_pi_tuple)

# Dictionary

ChhatraProperty = {
    'Name': 'Chhorm Chhatra' ,
    'Age': 19 ,
    'Entertainment' : 'Chatting and Watching Movies'

}
print(ChhatraProperty)
print(ChhatraProperty['Name'])

ChhatraProperty['Entertainment'] = 'Listening to the music'
print(len(ChhatraProperty))
print(ChhatraProperty.get('Age'))
print(ChhatraProperty.keys())
