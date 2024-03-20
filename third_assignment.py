"""
#1
10 marks
Complete the register_student function.
It should receive student's information. The arguments will be passed in the order: name, age, phone_number, email, spoken_languages
All elements will be strings 
In the place of 'spoken_languages' can be included ONE OR MORE languages. If no language specified, the default value will be "English" 

Your job is to create a dictionary using the keys:"name","age","phone_number","email","spoken_languages" that will mapp the given values to a dictionary.
All the values in the dictionary should be a string, except the value for the key 'spoken_languages' that will be a set of all the given languages

Input: strings
Output: dictionary

EXAMPLES:

example input: register_student("John Smith", "28", "1234567890", "john.smith123@am.amrita.edu", "English", "Hindi", "Tamil", "Malayalam")
example output: {'age': '28',
 'email': 'john.smith123@am.amrita.edu',
 'name': 'John Smith',
 'phone_number': '1234567890',
 'spoken_languages': {'Tamil', 'Malayalam', 'English', 'Hindi'}}
 
example input: register_student("Priya Sharma", "23", "8765432109", "priya123@am.amrita.edu")
example output: {'age': '23',
 'email': 'priya123@am.amrita.edu',
 'name': 'Priya Sharma',
 'phone_number': '8765432109',
 'spoken_languages': {'English'}}

Note: The example output was put in different lines for clarity, but your program will return a dictionary that is a single line
"""

def register_student(name, age, phone_number, email, *spoken_languages):
    if not spoken_languages:
        spoken_languages = {'English'}
    else:
        spoken_languages = set(spoken_languages)
    student_info = {
        "name": name,
        "age": age,
        "phone_number": phone_number,
        "email": email,
        "spoken_languages": spoken_languages}
    return student_info


"""
#2
9 marks
Complete the age_selector function that accepts an infinite amount of keyword arguments.
Each key will be the name of a person and the value will be it's age. 
Your job is to separate 2 groups: child or adult. If age is less than 18, is considered child.
Your function will select only adults, so it will return a set with the names of all the adults

input: keyword arguments "name1"=age1,"name2"=age2,"name3"=age3, ...., "nameN"=ageN
Output: Set of strings

example input: age_selector(michael=14,julia=19,bob=18,martin=40,jose=5)
example output: {'martin', 'julia', 'bob'}
"""
def age_selector(**kwargs):
    child = set()
    adult = set()
    for k,v in kwargs.items():
        if v < 18:
            child.add(k)
        else:
            adult.add(k)
    return adult

"""                                                                                                                     
#3
9 marks
Write the function nested_alphabet that prints the alphabet in a triangle shape. This will be 
accomplished by generating nested lists. Your function will only receive an integer as input.
It will include 1 element in the first list, 2 in the second one and so one until including 
as many letters in the base of the triangle as given in the input. If you run out of letters 
(in case of a high number as input), just begin the alphabet again!

example input: 5
example output:

 [['a'], 
 ['b', 'c'], 
 ['d', 'e', 'f'], 
 ['g', 'h', 'i', 'j'], 
 ['k', 'l', 'm', 'n', 'o']]

 
example input: 10
example output:
 [['a'], 
 ['b', 'c'], 
 ['d', 'e', 'f'], 
 ['g', 'h', 'i', 'j'], 
 ['k', 'l', 'm', 'n', 'o'], 
 ['p', 'q', 'r', 's', 't', 'u'], 
 ['v', 'w', 'x', 'y', 'z', 'a', 'b'], 
 ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 
 ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'], 
 ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']]
 
example input: 1
example output: [['a']]

example input: 0
example output: []

NOTE: the spaces between the letters do not matter, also the new lines don't matter. 
I added them to make the example clear - your output is just a list of lists with letters inside.
"""

def nested_alphabet(n):
    result = []
    start = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  
    for i in range(0, n):
        row = []
        #result.append(row)  
        for j in range(i+1):
            letter = alphabet[start % 26]  
            row.append(letter)
            start +=1
        result.append(row)
    return result 

print(nested_alphabet(5))

"""
#4
12 marks
Write a class to represent bank cards

instance attributes:
    
    balance: float
        # Amount of money with which the account is opened     
    card_brand: str
        # 'flash' or 'wire' EXACTLY, as the automated tester will use this words to define the object 
        # and your method should recognize them properly
        
        # For 'flash' cards there will be a 1% comission in the withdraw
        # For 'wire' cards there will be a 2% comission in the withdraw
        
methods:
    deposit: float
        returns: A float, the new balance of the account
    
    withdraw: float
        This function receives as an input the amount to be withdrawn 
        Then it should also include the respective comission over that amount, 
        Check first and only if the available balance is enough, perform the transaction.
            
            - If the final amount to be withdrawn is greater to the available balance it should return a 
        STRING message saying EXACTLY: "insufficient funds" . (The automated tester will check for exact value, 
        if you make a mistake in the spelling of this message, the question will be grade as wrong)
        
            - If the amount in balance is enought it should return a FLOAT, the REMAINING BALANCE after withdrawing.
            
EXAMPLE:

my_card=Card(10000,'flash')

example input: my_card.deposit(3500)
example output: 13500.0

and then apply the next method:

example input: my_card.withdraw(12000)
example output: 1380.0
   
"""

class Card:
    
    def __init__(self, balance, card_brand):
        self.balance = float(balance)
        self.card_brand = card_brand

    def deposit(self, desposit_amount):
        self.balance += desposit_amount
        return self.balance
    
    def withdraw(self, withdraw_amount):
        
        if self.card_brand == 'flash':
            withdraw_commission = 0.01
        elif self.card_brand == 'wire':
            withdraw_commission = 0.02
        total_amount = withdraw_amount + withdraw_amount*withdraw_commission
        if total_amount > self.balance:
            return "insufficient funds"
        else:
            self.balance -= total_amount
            return self.balance

"""
#5

12 marks
Inherit the given 'Car' class to create an 'Ambulance' class that will have some specialized behaviours

The new 'Ambulance' class will not have new attributes.

methods:
    The new 'Ambulance' class must inherit the Car class and add 2 more methods (with this exact names): 'reverse' and 'reach_nearest_hospital'

    - In 'reverse', the fuel consumption should be 13 km/liter for any kind of vehicle (2wd and 4wd). This method will modify the 
    instance attribute 'available_fuel' but will return None
    Input: Integer
    Output: None
    
    - 'reach_nearest_hospital' will receive an integer as argument and drive fast (using the inherit function of the parent class) and if don't have enough fuel, 
    it should stop for fuel on the way. This function will return the 2 possible messages:
        - "Reached without stops" if the fuel was enough to reach
        - "Made a stop to fill gas" if the fuel was not enough to reach
    Input: Integer
    Output: String
    
EXAMPLES:
input_A : 
ambulance1=Ambulance(35,True) # An object is created by the grader (with 35 liters of fuel and is 4wd)
ambulance1.drive_off_road(20) # Some methods are applied to it
ambulance1.reverse(5)         # Some methods are applied to it
(round(ambulance1.available_fuel,0) # Check the available fuel of the ambulance 

output_A : 29.0

input_B : ambulance2=Ambulance(18,False).reach_nearest_hospital(60) # Creates an object and drive it to the hospital
output_B: Reached without stops

input_C : ambulance3=Ambulance(20,False).reach_nearest_hospital(65)
output_C: Reached without stops

"""
class Car:
    def __init__(self, available_fuel, is_4wd):
        self.available_fuel = available_fuel
        self.is_4wd = is_4wd

    def drive_fast(self, distance):
        if self.is_4wd:
            fuel_consumption = distance * 1.5  / 5  
        else:
            fuel_consumption = distance * 1.5 / 10   
            
        if fuel_consumption <= self.available_fuel:
            self.available_fuel -= fuel_consumption
            print(f"The car drove {distance} km fast. 4WD: {'Yes' if self.is_4wd else 'No'}, Available fuel: {self.available_fuel} liters")
            return(fuel_consumption)
        else:
            self.available_fuel -= fuel_consumption # It's fine if this number is negative, It will indicate the needed fuel
            print("Not enough fuel for the trip. Refil required.")
            return(fuel_consumption)

    def drive_off_road(self, distance):
        if self.is_4wd:
            fuel_consumption = distance* 1.3/5  # 1.3 liters per 5 km when driving off-road
            if fuel_consumption <= self.available_fuel:
                self.available_fuel -= fuel_consumption


class Ambulance(Car):

    def reverse(self, distance):
        fuel_consumption = distance * 1 / 13
        self.available_fuel -=fuel_consumption
        return None

    def reach_nearest_hospital(self, distance):
        fuel_needed = self.drive_fast(distance)
        if fuel_needed <= self.available_fuel:
            return("Reached without stops")
        else:
            self.available_fuel += fuel_needed
            return("Made a stop to fill gas")

ambulance1=Ambulance(35,True) # An object is created by the grader (with 35 liters of fuel and is 4wd)
ambulance1.drive_off_road(20) # Some methods are applied to it
ambulance1.reverse(5)         # Some methods are applied to it
#(round(ambulance1.available_fuel,0) # Check the available fuel of the ambulance 

