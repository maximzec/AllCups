from typing import Dict

special_value = -1

def print_dict(first, last, dict):
    for i in range(first, last + 1):
        print(i, dict[i])

def init_dict(first_key, last_key):
    dict = {}
    for i in range(first_key, last_key + 1):
        dict[i] = special_value
    return dict

def input_many_int_vals():
    return [int(num) for num in input().split()]

 
first_day, last_day, current_day, db_records_count = input_many_int_vals()
#database = init_dict(first_day, last_day)
database = {}
for i in range(db_records_count):
    day, value = input_many_int_vals()
    database[day] = value
"""
for day in database.keys():
    if day <= current_day:
        if database[day] == -1:
            for day_prev in database.keys():
                if day_prev == day:
                    break
                database[day] = database[day_prev]
    """ 
#if first_day not in database.keys():
#    database[first_day] = -1

for day in range(first_day, last_day + 1):
    if day > current_day:
        database[day] = -1
    if day not in database.keys():
        database.setdefault(day,database.get(day - 1, -1))

print_dict(first_day, last_day, database)