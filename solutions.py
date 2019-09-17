## my in class practice with doctest

# could also just create
# time_dict = {}

time_dictionary  = dict(hours='', minutes='', seconds='')

# school['name']

def extract_time_components(time_string):
    #split time_string by ':'
    split_time = time_string.split(":")
    time_dictionary.update({'hours': int(split_time[0]), 'minutes': int(split_time[1]), 'seconds': int(split_time[2])})
    print(split_time)
    print("------" * 3)
    print(time_dictionary)


'''
>>> extract_time_components('21:30:00')
{'hours': 21, 'minutes': 30, 'seconds': 0}
>>> extract_time_components('09:01:53')
{'hours': 9, 'minut
'''
# DEFINING THE PROBLEM AND MAKING STEPS
#take in a string that is a 24-hour time with 
#       the hour,       minutes, and        seconds 
#   seperated by `:`s
#
#  return a dictionary with corresponding integer values
#   keys 
#       `hour`,     `minutes`, and      `seconds` 
#               

extract_time_components('21:30:00')


## alt notes
hours, minute, seconds = s.split(':')
or
hours, minute, seconds = [int(n) for n in s.split(':')]

time_dict2 = {
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds)


}