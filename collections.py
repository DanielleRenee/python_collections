course = {'title': 'Python Collections', 'student': 'Danielle'}

course['student'] == 'Danielle'

course = {'title': 'Python Collections', 'student': {'first name': 'Danielle', 'middle name': 'Renee'}}

course['student']['first name'] == 'Danielle'

course['day'] = 'Friday'

course['color'] = 'Pink'

del course['day']

course.update({'day': 'Thursday', 'runtime': '80 minutes'})


"""Make a dictionary named player and add two keys to it. 
The first key should be "name" and the value can be any string you want.
The second key should be "remaining_lives". Set this key's value to 3."""

player = {'name': 'danielle', 'remaining_lives': 3}

"""Now add a "levels" key. It should be a list with the values 1, 2, 3, and 4 in it.
And, lastly, add an "items" key. This key's value should be another dictionary. 
Give it at least one key and value, but they can be anything you want."""

player['levels'] = [1, 2, 3, 4]
player['items'] = {'color': 'blue'}

"""Packing dictionaries"""

def packer(**kwargs):
    print(kwargs)


packer(name='danielle', num=31, meat=None)

# prints out {'meat': None, 'num': 31, 'name': 'danielle'}


def packer(name=None, **kwargs):
    print(kwargs)


packer(name='danielle', num=31, meat=None)

# prints out {'meat': None, 'num': 31}



"""Unpacking dictionaries"""

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print "Hi {} {}!".format(first_name, last_name)
    else: 
        print "Hi no name!"


unpacker(**{'last_name':'russell', 'first_name':'danielle'})

# call the function with the power of unpacking
# gave one single dictionary as the only argument. 
# didn't even need to name the dictionary, 
# took each key word argument in the dict and sent them as arguments to to function.
# **kwargs must be the last element passed in to the function.


"""Let's test unpacking dictionaries in keyword arguments.
If you give the placeholder a name, though, like in template below, 
you fill it in through keyword arguments to .format(), like this:
template.format(name="Kenneth", food="tacos") Write a function named 
string_factory that accepts a list of dictionaries as an argument. 
Return a new list of strings made by using ** for each dictionary 
in the list and the template string provided."""

template = "Hi, I'm {name} and I love to eat {food}!"
values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

def string_factory(values):

    result_list = []

# for each item in values (so each individual dictionary),
# grab the key word arguements using ** and pass each keyword
# in to the template via format method. 

    for i in values: 
        result_list.append(template.format(**i))

    return result_list

string_factory(values)
# prints out [
              # "Hi, I'm Michelangelo and I love to eat PIZZA!", 
              # "Hi, I'm Garfield and I love to eat lasagna!"
              # ]



# print out the keys in a dictionary
for key in course: 
    print key

for key in course.keys():
    print key

# print out the values in a dictionary
for key in course: 
    print course[key]

for value in course.values():
    print value

# get a list of tuples with keys and value from a dictionary
course.items()

# return key value tuples themselves
for item in course.items():
    print item


"""make a function named word_count. 
It should accept a single argument which will be a string. 
The function needs to return a dictionary. 
The keys in the dictionary will be each of the words in the string, lowercased. 
The values will be how many times that particular word appears in the string."""

def word_count(string):

    counts = {}

    for word in string.split(): 
        if word.lower() in counts:
            counts[word.lower()] += 1
        else: 
            counts[word.lower()] = 1

    return counts



"""For this first task, create a function named num_teachers that takes 
a single argument, which will be a dictionary of Treehouse teachers 
and their courses. The num_teachers function should return an integer 
for how many teachers are in the dict."""

dct = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
'Kenneth Love': ['Python Basics', 'Python Collections']}

def num_teachers(dct):

    return len(dct.keys())


def num_courses(dct):
    num = 0
    for i in dct.values():
        num += len(i)

    return num


def courses(dct):
    courses_list = []

    for i in dct.values():
        courses_list += i


def most_courses(dct):

    max_value = 0

    for teacher in dct.items():

        if len(teacher[1]) > max_value:
            max_value = len(teacher[1])
            busy_teacher = teacher[0]

    return busy_teacher


dct = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'Nell Basics'],
'Kenneth Love': ['Python Basics', 'Python Collections']}



"""In this last challenge, I want you to create a function named stats and 
it'll take our teacher dictionary as its only argument.
stats should return a list of lists where the first item in each inner list is 
the teacher's name and the second item is the number of courses that teacher has. 
For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]"""

def stats(dct):

    stat_list = []

    for item in dct.items():
        stat = []
        stat.append(item[0])
        stat.append(len(item[1]))

        stat_list.append(stat)

    return stat_list


# TUPLES
my_tuple = 1, 2, 3
# same as
my_same_tuple = (1, 2, 3)

my_third_tuple = (5,)
# not same as
my_int_not_tuple = (5)

# or can use the tuple function
my_fourth_tuple = tuple([1, 2, 3,])

# can't add, change value or reassign indexes for a tuple
# can however change value of an item inside of the tuple

# can count and and check index

tuple_with_a_list = (1, 'apple', [3, 4, 5])
tuple_with_a_list[2][0] = 2 

# can do whatever I want to the inside of the list inside the tuple,
# BUT cannot delete the list inside the tuple, because that would be changing the tuple. 

a = 5
b = 20 

# want to switch the values of a and b 
# little python magic

a, b = b, a

# python makes a tuple right after the equal sign.
# in that tuple were the values 20 and 5
# and then python unpacked that tuple in to two variables, a and b

"""packing tuples with *"""

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# add(5, 5) will return 10
# add(32) will return 32


# more common is to use args for the same outcome

def add(base, *args):
    total = base
    for num in args:
        total += num
    return total


# add(5, 20) will return 25

# with the exception of **kwargs, *args has come after any other params
# would need to be
# def add(*args, **kwargs):


def fun(*args):
    """simple args example"""
    for arg in args:
        print arg

my_list = [4, 5, 'apple', 'blue', 2]

fun(my_list) 
# will print out the list in tact
# but if I call 
fun(*my_list) 
# it will take all the items 
# in my list as arguments and pass them in and therefore print 
# each item in the list out


"""Create a function named multiply that takes any number of arguments. 
Return the product (multiplied value) of all of the supplied arguments. 
The type of argument shouldn't matter."""

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total



"""Create a function that takes in a string and returns a tuple of
versions of that string. Uppercase, lowercase, title case and reversed string."""

def stringcases(string):
    return string.upper(), string.lower(), string.title(), string[::-1]




"""Create a function named combo that takes two ordered iterables. 
These could be tuples, lists, strings, whatever. Your function should return a 
list of tuples. Each tuple should hold the first item in each iterable, 
then the second set, then the third, and so on. 
Assume the iterables will be the same length.
Check the code below for an example."""

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(a, b):
   new_list = []
   
   for i in range(len(a)):
    new_list.append((a[i], b[i]))

    return new_list



"""Set math"""

songs = {'songy song','darling song','sweets song'}

songs.add('Treehouse Hula')

songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})

# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - returns a new set of all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
# (also: notice how those are using *others? That's a tuple of other sets.)

# can do them all as operators and methods

set1 = set(range(10))

set2 = {1, 2, 3, 5, 7, 9, 11, 13, 17, 19, 23}

>>> set1.union(set2)
set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23])

>>> set2 - set1
set([19, 17, 11, 13, 23])



"""So, first, write a function named covers that accepts a single parameter, 
a set of topics. Have the function return a list of courses from COURSES 
where the supplied set and the course's value (also a set) overlap.
For example, covers({"Python"}) would return ["Python Basics"]."""


COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(topics):
    courses_list = []   

    for course in COURSES:
        
        if COURSES[course] & topics:   # Here the & sign finds the overlaps of the two sets.
            courses_list.append(course)

    return courses_list























