from pathlib import Path
"""                                                                                                                     
#1
9 marks
Write a function that accepts a single list of strings it should filter it.
You should return 3 separate lists, each one of which contains a certain category of strings 
Categories:
    number_only_list : the string contains only digits like: "123"
    letter_only_list : the string contains only letters like: "abc"
    full_mix_list : the string contains anything like: "https://my_website.com/%00/etc/passwd"

You need to return all three lists in a tuple with the follow order:
(number_only_list, letter_only_list, full_mix_list)
In each sublist the elements should be in the same order of appereance as in the initial list.

example input: ["123","1asd23","manzanas","128753","other language","ajsh.saso"]
example output: (['123', '128753'], ['manzanas'], ['1asd23', 'other language', 'ajsh.saso'])

example input: ["123","6","3038"]
example output: (['123', '6', '3038'], [], [])

Note: the space character " " counts as something else than letter, so it should go in the full_mix_list
If a type of string is missing from the input (i.e: no strings with numbers only are found) you should return an empty list for that type

"""

def sort_by_component(input_list):
    number_only_list = []
    letter_only_list = []
    full_mix_list = []
    for i in input_list:
        if i.isdigit():
            number_only_list.append(i)
        elif i.isalpha():
            letter_only_list.append(i)
        else:
            full_mix_list.append(i)
    return (number_only_list, letter_only_list, full_mix_list)

"""
#2
9 marks
Write a function that accepts an infinite amount of positional arguments
All the inputs will be integers.
Your function should take all the arguments and place them into tuples of 
4 elements each. 
Each tuple will have the following structure:
(first_element,"and",second_element,first_element+second_element)
Put all the tuples in a list, return the list.

In case you receive an odd amount of arguments, fill the last sum with 0 
(the number zero)

Input: Integers
Output: List of Tuples

example input:  infinite_sums(1,2,3,4,5,6,7,8)
example output: [(1, 'and', 2, 3), (3, 'and', 4, 7), (5, 'and', 6, 11), (7, 'and', 8, 15)]

example input:  infinite_sums(33, -30, 21, 15, 35, 58, -31)
example output: [(33, 'and', -30, 3), (21, 'and', 15, 36), (35, 'and', 58, 93), (-31, 'and', 0, -31)]
"""

def infinite_sums(*args):
    result = []
    if len(args)%2==1:
        args += (0,)
    for i in range(0,len(args), 2):
        sum = args[i] + args[i + 1]
        result.append((args[i], 'and', args[i+1], sum))
    return result

"""
#3
9 marks
Complete the function vowel_consonant_counter. This function recevies a string in lowercase as an input and 
creates a dictionary counting how many vowels and how many consonants the string have.
If ANY CHARACTER THAT IS NOT A LETTER appears (like "!" "@" "." "," "&") it should not be counted
in any category.

The name of the keys in the dictionary should be exactly 'vowel' for the vowels 
and 'consonant' for the consonant

Input: String
Output: Dictionary

example input: "apples"
example output: {'vowel': 2, 'consonant': 4}

example input: "islands in pacific are home to seven major mountain ranges that have peaks of over 1000 metres."
example output: {'vowel': 31, 'consonant': 43}

"""

def vowel_consonant_counter(string):
    sample = {'vowel':0, 'consonant':0}
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    for i in string:
        for j in vowel:
            if i == j:
                sample['vowel']+=1
        for j in consonant:
            if i == j:
                sample['consonant']+=1
    return sample

"""
#4
9 marks
Complete the folder_description function that creates a dictionary mapping each datatype to the amount
of files present in that folder. 
Your function will receive one input: folder_name
It will return a dictionary in which the key represents the file type (".doc",".pptx",".docx",".pdf",".txt", etc....)
and the value represents how many files of each type is present in that folder. Your dictionary should only map to the present extensions in that folder
(if there is no pdf files, it should not have a key for ".pdf")

Note: I am including this two folders 'my_desktop' and 'video_dic' as downloadables so you can practice.
You only have to upload this python script in Autolab.
A set of folders with different files will be loaded in the Autolab server for the testcases

Input: String
Output: Dictionary

EXAMPLES:
input_A : folder_description("my_desktop")
output_A : {'.pdf': 3, '.jpg': 3, '.csv': 2}

input_B : folder_description("video_dic")
output_B: {'.jpg': 6, '.pdf': 6, '.csv': 4}

"""
def folder_description(folder_to_inspect):
    file_type_count = {}
    folder_path = Path(folder_to_inspect)
    for i in folder_path.iterdir():
        if i.is_file():
            file_type = i.suffix.lower()
            if file_type:
                file_type_count[file_type] = file_type_count.get(file_type, 0) + 1
    return file_type_count



"""
#5
9 marks
Make a function that will inspect a folder and will return all the file names of a specific type. 
Your function will receive two inputs: folder_name and file_type
It will return a set of strings. Each string will be the name of the file (including the extension)

Input: String , String
Output: Set of Strings

EXAMPLES:

input_A : folder_inspector("my_desktop",".pdf")
output_A : {'shoping_list.pdf', 'test.pdf', 'travels.pdf'}

input_B : folder_inspector("my_desktop",".csv")
output_B: {'SampleCSVFile_2kb.csv', 'SampleCSVFile_11kb.csv'}

"""
def folder_inspector(folder_to_inspect, filetype_to_inspect):
    matching_files = set()
    folder_path = Path(folder_to_inspect)
    for i in folder_path.iterdir():
        if i.is_file() and i.suffix.lower() == filetype_to_inspect:
            matching_files.add(i.name)
    return matching_files