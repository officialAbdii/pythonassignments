"""
#1

8 marks
Complete the organizer function.
It should receive a list of numbers and order ascending in a new list.
If a number appears more than one time, just put it once

Input: List
Output: List

EXAMPLES:

example input: [1, -27, 28, 2, -28, 1, -17, -20] 
example output: [-28, -27, -20, -17, 1, 2, 28]

example input: [-10, -24, 8, -15, -30, -10, 28, -10, 20, -25, -27, 2, 18, -15, 21, 17, -6, 19, -2, 7]
example output: [-30, -27, -25, -24, -15, -10, -6, -2, 2, 7, 8, 17, 18, 19, 20, 21, 28]
"""

def organizer(given_list):
    sorted_list = []
    for i in given_list:
        if i not in sorted_list:
            sorted_list.append(i)
    sorted_list.sort()
    return sorted_list

"""
#2

8 marks
Make an invitation maker function.
It should receive a dictionary with they keys: "first_name","last_name","companions","topic"
It should return a generic STRING including the specific details of that person.

Input: Dictionary
Output: String

EXAMPLES:

example input: {'first_name': 'Bob', 'last_name': 'Singh', 'topic': 'Artificial intelligence'} 
example output: Hello Mr./Ms. Bob Singh, we are very happy to have your talk on Artificial intelligence!

example input: {'first_name': 'Anne', 'last_name': 'Vilaz', 'companions': 3, 'topic': 'Astrophysics'} 
example output: Hello Mr./Ms. Anne Vilaz, we are very happy to have your talk on Astrophysics!
"""

def invitation_maker(dictionary):
    first_name = dictionary.get('first_name', '')
    last_name = dictionary.get('last_name', '')
    topic = dictionary.get('topic', '')
    invitation = f"Hello Mr./Ms. {first_name} {last_name}, we are very happy to have your talk on {topic}!"
    return invitation

invitation_maker({'first_name': 'Bob', 'last_name': 'Singh', 'topic': 'Artificial intelligence'})

"""
#3

12 marks
Make a vowel counter.
It will receive a string as input.
It will count how many times each vowel appears and retun a dictionary with the vowels as keys and number of repetitions as values.

Input: String
Output: Dictionary

EXAMPLES:

example input: "Where there's a will, there's a way."
example output: {'a': 3, 'e': 6, 'i': 1, 'o': 0, 'u': 0}

example input: "Don't count your chickens before they hatch."
example output: {'a': 1, 'e': 4, 'i': 1, 'o': 4, 'u': 2}
"""

def vowel_counter(user_input):
    vowel_a=0
    vowel_e=0
    vowel_i=0
    vowel_o=0
    vowel_u=0
    for i in user_input:
        if i == 'a':
            vowel_a+=1
        if i == 'e':
            vowel_e+=1
        if i == 'i':
            vowel_i+=1
        if i == 'o':
            vowel_o+=1
        if i == 'u':
            vowel_u+=1
    vowel_counts_dict = {
    'a': vowel_a,
    'e': vowel_e,
    'i': vowel_i,
    'o': vowel_o,
    'u': vowel_u}
    return (vowel_counts_dict)

vowel_counter('my name is abdeali merchant')

"""
#4

9 marks
Make a function that finds the common elements of two lists. 
It will receive two arguments. Each one of them a list.
Each list will have the names of different countries.
Your function should identify the countries that are only in both lists and return a set with these countries.
If there is no common countries in the two lists, it should return an empty set

Input: Two Lists of Strings
Output: Set

example input: common_countries(['Sri Lanka', 'Mongolia', 'Switzerland', 'Namibia', 'Gambia', 'Bhutan', 'Israel', 'Yemen', 'Togo',
'Ukraine', 'Turkey', 'Vanuatu', 'Belgium', 'Seychelles', 'Turkmenistan', 'Djibouti', 'Jamaica', 'Cameroon', 'Thailand', 'Sao Tome and Principe',
'Croatia', 'New Zealand', 'Antigua and Barbuda', 'Barbados', 'Niger', 'Vietnam', 'Burundi', 'Zambia', 'Dominican Republic', 'Austria', 'Saint Lucia',
'Jamaica', 'Uganda', 'Moldova', 'Saint Kitts and Nevis'],
['Guatemala', 'Democratic Republic of the Congo', 'Liberia', 'Malta', 'Kuwait', 'Greece', 'Eswatini', 'Greece', 'Papua New Guinea', 'Mauritania',
'Ghana', 'Georgia', 'Senegal', 'Czechia (Czech Republic)', 'Germany', 'Hungary', 'New Zealand', 'Thailand', 'Indonesia', 'Barbados',
'Spain', 'Bhutan', 'United Arab Emirates', 'New Zealand', 'Uruguay', 'Kiribati', 'Tuvalu', 'Palestine State', 'Latvia', 'Dominica', 'Ghana',
'Palestine State', 'Malta', 'Venezuela', 'Philippines', 'France', 'Philippines', 'Saudi Arabia', 'Central African Republic', 'Nigeria',
'Slovenia', 'Jamaica', 'Sao Tome and Principe', 'Eswatini', 'Zambia', 'Tajikistan', 'Azerbaijan', 'Democratic Republic of the Congo',
'Cameroon', 'South Korea', 'Nauru'])

example output: {'New Zealand', 'Zambia', 'Barbados', 'Cameroon', 'Sao Tome and Principe', 'Thailand', 'Bhutan', 'Jamaica'}


example input: common_countries(['Portugal', 'Brunei', 'Saint Vincent and the Grenadines', 'Andorra', 'Maldives', 'San Marino',
'Papua New Guinea', 'Fiji', 'Azerbaijan', 'Eswatini', 'Belize', 'Thailand', 'Latvia', 'Croatia', 'Honduras', 'Bahamas'],
['Cuba', 'Saint Lucia', 'Guinea', 'Mexico', 'Gabon', 'Denmark', 'Qatar', 'Kuwait', 'Barbados', 'Burundi', 'Australia',
'Gambia', 'Dominican Republic', 'Guyana', 'Peru', 'Ivory Coast', 'Sri Lanka', 'Argentina', 'Greece', 'Latvia', 'Sri Lanka',
'Switzerland', 'Saudi Arabia', 'Senegal', 'Turkmenistan', 'Kenya', 'Venezuela', 'Yemen'])

example output: {'Latvia'}
"""

def common_countries(list1,list2):
    common_countries_list = []
    for i in list1:
        for j in list2:
            if i == j:
                common_countries_list.append(i)
    common_countries_set = set(common_countries_list)
    return common_countries_set

common_countries(['Sri Lanka', 'Mongolia', 'Switzerland', 'Namibia', 'Gambia', 'Bhutan', 'Israel', 'Yemen', 'Togo',
'Ukraine', 'Turkey', 'Vanuatu', 'Belgium', 'Seychelles', 'Turkmenistan', 'Djibouti', 'Jamaica', 'Cameroon', 'Thailand', 'Sao Tome and Principe',
'Croatia', 'New Zealand', 'Antigua and Barbuda', 'Barbados', 'Niger', 'Vietnam', 'Burundi', 'Zambia', 'Dominican Republic', 'Austria', 'Saint Lucia',
'Jamaica', 'Uganda', 'Moldova', 'Saint Kitts and Nevis'],
['Guatemala', 'Democratic Republic of the Congo', 'Liberia', 'Malta', 'Kuwait', 'Greece', 'Eswatini', 'Greece', 'Papua New Guinea', 'Mauritania',
'Ghana', 'Georgia', 'Senegal', 'Czechia (Czech Republic)', 'Germany', 'Hungary', 'New Zealand', 'Thailand', 'Indonesia', 'Barbados',
'Spain', 'Bhutan', 'United Arab Emirates', 'New Zealand', 'Uruguay', 'Kiribati', 'Tuvalu', 'Palestine State', 'Latvia', 'Dominica', 'Ghana',
'Palestine State', 'Malta', 'Venezuela', 'Philippines', 'France', 'Philippines', 'Saudi Arabia', 'Central African Republic', 'Nigeria',
'Slovenia', 'Jamaica', 'Sao Tome and Principe', 'Eswatini', 'Zambia', 'Tajikistan', 'Azerbaijan', 'Democratic Republic of the Congo',
'Cameroon', 'South Korea', 'Nauru'])


