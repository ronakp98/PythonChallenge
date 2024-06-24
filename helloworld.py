#   Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple



# Exercise: Level 3
# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

# Integer
3
# Float
3.24
# Complex
k = 3
k + 3
# String
'Coding is Fun'
# Boolean
True
# List
[0, 1, 2, 3, 4]
# Tuple
('Up', 'Down', 'Left', 'Right')
# Set
{3, 7, 8, 12, 15}
# Dictionary
{
    'first_name':'Ron',
    'last_name':'Patel',
    'age': 26
}


# 2. Find an Euclidian distance between (2, 3) and (10, 8)

EDistance = 0

EDistance = (((10 - 2) ** 2) + ((8-3) ** 2)) ** 0.5
print(EDistance)