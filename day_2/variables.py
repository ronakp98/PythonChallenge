# Day 2: 30 Days of python Programming

#Exercises: Level 1

first_name = 'Ron'
last_name = 'Patel'
full_name = 'Ron Patel'
country = 'USA'
city = 'RDU'
age = 26
year = 2024
is_married = False
is_true = True
is_light_on = False
current_month, current_day, current_year = 6, 27, 2024


#Exercises: Level 2
type(first_name),
type(last_name),
type(full_name),
type(country),
type(city),
type(age),
type(year)
type(is_married)
type(is_true)
type(is_light_on)

print(len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two

import math

circle_radius = 30
area_of_circle = math.pi * pow(circle_radius, 2)
print(area_of_circle)
circum_of_circle = 2 * math.pi * circle_radius
print(circum_of_circle)


user_first_name = input('What is your first name: ')
user_last_name = input('What is your last name: ')
user_country = input('What is your country: ')
user_age = input('What is your age: ')

print('FN', user_first_name, '\nLN', user_last_name, '\nCountry', user_country, '\nAge', user_age)