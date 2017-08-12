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





























