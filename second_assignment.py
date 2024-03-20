"""
#1

10 marks
Complete the even_list function.
It should receive a variable number of arguments. The arguments will all be integers.
It will create a list with all the even numbers and sort it ascending.
It will return that list.

Input: integers
Output: list

EXAMPLES:

example input: even_list(24, 15, 19, 17, 5, 9, 11, 1, 4, 2, 22, 14, 10, 7, 18, 16, 8)
example output: [2, 4, 8, 10, 14, 16, 18, 22, 24]

example input: even_list(30, 38, 27, 40, 54, 15, 25, 43, 48, 44, 16, 45, 35, 42, 22, 13, 17, 39, 50, 28, 36, 18, 32, 47, 31, 57, 33, 19, 55, 51, 53)
example output: [16, 18, 22, 28, 30, 32, 36, 38, 40, 42, 44, 48, 50, 54]
"""

def even_list(*args):
    even_list = []
    for i in args:
        if i%2==0:
            even_list.append(i)
    even_list.sort()
    return even_list

"""
#2

12 marks
Finish the type_assign function.
It should take a list elements of any type (int, float, string, list, tuple, set, dictionary)
and return a dictionary counting how many of each element is given in the input list.
Where the key is EXACTLY the datatype NAME (refer to the examples) and the value is the number of appearances. 

Input: list
Output: dictionary

EXAMPLES:
input_A : [1, 70, 2, 84, 15, 36, 14]
output_A : {'int': 7, 'float': 0, 'string': 0, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}

input_B : ['Hello you', 85.41, 7, 4.0, 'another string']
output_B : {'int': 1, 'float': 2, 'string': 2, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}

input_C : ['one', {'sugar':5, 'flour':4, 'oils':17}, 7, (84, 8880, 4236), 42.5, 5, 'two', 68, {1, 2, 3}, {78, 45, 48}]
output_C : {'int': 3, 'float': 1, 'string': 2, 'list': 0, 'tuple': 1, 'set': 2, 'dictionary': 1}

"""
def type_assign(num_list):
    type_count = {'int': 0, 'float': 0, 'string': 0, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}

    for i in num_list:
        data_type = type(i).__name__
        if data_type == 'str':
            type_count['string'] += 1
        elif data_type == 'dict':
            type_count['dictionary'] += 1
        elif data_type in type_count:
            type_count[data_type] += 1
    
    return type_count

"""
#3

12 marks

Write a function `password_check` to check the validity of a password. 
Return True if valid, False otherwise
  
Validation : 
Only letters (uppers and lowers), digit, and the symbols in the list [#, $, @] are allowed

At least 1 letter between [a-z] and 1 letter between [A-Z]. 
At least 1 digit from [0-9]. 
At least 1 character from [$#@]. 
Special characters not in the list of [$#@] are not allowed.
Minimum length 6 characters. 
Maximum length 10 characters. 

Input: string
Output: boolean

Examples:
Input: "amaZZ1_"
Output: False  (not valid)

Input: "aazzZZ12$$"
Output : True 

Input: "azZ1$"
Output: False  (too short)

Input: "a$gh1$123Af"
Output: False  (too long)

hint:
Search about the string functions: .isupper(), islower(), isdigit()
"""

def password_check(password):
    if 6 <= len(password) <= 10 and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in ['#', '$', '@'] for char in password) and all(char.isalpha() or char.isdigit() or char in ['#', '$', '@'] for char in password):
                    return True
    else: 
        return False
             


"""
#4

12 marks
Finish the swap_string function.
It should swap the adjacent characters in a string and add space after each pair,
if no swapping partner is present, just add space 

Input: String
Output: String

EXAMPLES:
input_A : "arvcwevw"
output_A : "ra cv ew wv"

input_B : "bsvcdwe"
output_B:  "sb cv wd  e"  (Notice the double space before the last character)

input_C : "bswv325wev"
output_C: "sb vw 23 w5 ve"

"""

def swap_string(string):
    new_string = ""
    swapped_string = ""
    if len(string)%2==1:
        new_string = string + " "
    else:
        new_string = string 
    for i in range(0, len(new_string), 2):
        swapped_string += new_string[i+1] + new_string[i] + " "

    return swapped_string.rstrip()

"""
#5

7 marks
Finish the even_sum function.
It should return the sum of values having even key, if no even key 
return 0

Input: dictionary
Output: integer Result

EXAMPLES:

input_A : {1:"45",7:"12",34:"765"}
output_A : 765

input_B : {4:"5",43:"342",72:"7"}
output_B:  12

input_C : {1:"23"}
output_C: 0

"""

def even_sum(dic):
    sum = 0
    for k,v in dic.items():
        if k%2==0:
            sum += int(v)

    return sum