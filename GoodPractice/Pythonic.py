# https://gist.github.com/JeffPaine/6213790
# xrange over range :
for i in [0 , 1 , 2 , 3 , 4 , 5]:
    print (i ** 2)

for i in range (6):
    print (i ** 2)
# xrange is not supported in python 3
# for i in xrange(6):
#     print(i**2)


# Looping over a collection
colors = ['Blue' , 'Green' , 'Yellow' , 'Pink' , 'White', 'Blue', 'Maroon', 'Pink', 'White', 'Green', 'Blue', 'White']
for i in range (len (colors)):
    print (i , colors[i])
# Better to use :
for color in colors:
    print (color)

# Looping backward
# range(start, stop, step)
# start from which index
# stop before what index
# how many steps to go
for i in range (len (colors) - 1 , -1 , -1):
    print (i , colors[i])
# Better
for color in reversed (colors):
    print (color)

# Looping over a collection and indices (plural form of index)
for i in range (len (colors)):
    print (i , '-->' , colors[i])
# Better
for i , color in enumerate (colors):
    print (i , '-->' , color)

# Looping two collections
# zip() to group collections according to each other
names = ['Tech' , 'No' , 'Log' , 'Gii']
ages = ['29' , '28' , '27' , '26' , '30']
zipped = zip (names , ages)
zipped_list = list (zipped)
print (zipped_list)
# 2 ways to loop over two collections
# way 1
n = min (len (names) , len (ages))
for i in range (n):
    print (names[i] , ages[i])
# way 2 (for python 3, zip is the izip in python 2)
for name , age in zip (names , ages):
    print (name , age)
# for python 2, there is a way called zip (which is not the zip in python 3)
# zip in python 2 will create a new list in memory
# izip in python 2 or zip in python 3 is more efficient
# for name, age in izip(names, ages)
#     print(name, age)

# loop in sorted order
for name in sorted (names):
    print (name)
for name in sorted (names , reverse=True):
    print (name)


# custom sort order in python

# for python 2:
# def compare_len(c1 , c2):
#     if len (c1) < len (c2): return -1
#     if len (c1) > len (c2): return 1
#     return 0
# print (sorted(names, cmp=compare_len))
# better :
print(sorted(names, key=len))

# Calling a function until meeting the sentinel value
blocks = []
while True:
    block = input()
    print(block)
    if block == '!':
        break
    blocks.append(block)
print(blocks)
# better way is to use iter which take two argument (iterate function, flag or sentinel value)
# blocks =[]
# with block in iter(input(), '!'):
#     blocks.append(block)
# print(blocks)

# Introduce multiple break points - by using for-else
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i
def find_better(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
for name in names:
    if(name == 'Derek'): break
for name in names:
    if(name =='K'): break
else : print("You see this because of for-else")

# iterate throw dictionary
dic = {
    'Name' : 'Darson',
    'Age' : '29',
    'Occupation' : 'Programmer',
    'Job' : 'Project Manager',
    'King' : True
}
# first way
for key in dic :
    print(key, dic[key])
# second way : used when mutating the dictionary during the iteration
# in python 3, dic.keys() will return the dict_keys([]) view, make it into list to use it
print(dic.keys())
print(list(dic.keys()))
for key in list(dic.keys()):
    if key.startswith('K') : del(dic[key])
print(dic)

# other way to iterate item and key
for key, value in dic.items():
    print(key, value)
# NB : in python 2: items () will make a huge big list, to solve that, iteritems() was introduced
# NB : in python 3: items() and iteritems() have the same behaviour


# Construct dictionary from pair
new_dic = dict(zip(names, colors))
print(new_dic)

# counting with dictionaries
# counting from list into dictionary
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
# best practice
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

# counting list, add list item into dictionary
d = {}
for color in colors:
    key = len(color)
    d.setdefault(key, []).append(color)
print(d)

# Updating multiple state variables
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print (x)
        t = y
        y = x + y
        x = t
# better to use :
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print (x)
        x, y = y, x + y
# because x, y should be updated at the same state
# Simultaneous Update

# String Concatenation in list
# it's better to use .join() rather than +
# join the first string into the items in the list
print((', ').join(names))

# for python 2: use deque to fasten append and pop on either end int in the list
usernames = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
# bad practice
del usernames[0]
# The below are signs you're using the wrong data structure
print(usernames.pop(0))
# pop - remove and return the element in the given position,
# if the position is not found, it will remove the last item and return it
usernames.insert(0, 'mark')
print(usernames)
# better practice for python 2
# names = deque(['raymond', 'rachel', 'matthew', 'roger',
#                'betty', 'melissa', 'judith', 'charlie'])
#
# # More efficient with deque
# del names[0]
# names.popleft()
# names.appendleft('mark')

# To open and close file
# f = open('Sample.txt')
# try:
#     data = f.read(32)
#     print('read file')
# finally:
#     f.close()
# with open('data.txt') as f:
#     data = f.read()
#     print(data)
# New-way to use a lock
# with lock:
#     print 'Critical section 1'
#     print 'Critical section 2'

result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print (sum(result))
# better way
print(sum(i**2 for i in range(10)))