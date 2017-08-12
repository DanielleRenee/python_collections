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
