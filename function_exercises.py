### This is my first PYTHON "FUNCTION" exercises file

## Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function

# 1.- Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise

def is_two(input):
    if input == 2:
        return True
    elif input == "2":
        return True
    else:
        return False

#print(is_two(3))

## 2.- Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise

def is_vowel(string):
    if string in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False
#print(is_vowel("b"))

## 3.- Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this

def is_consonant(string):
    if string not in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False
is_consonant("b")
#print(is_consonant("b"))

## 4.- Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant

def change_first_consonant(string):
    if string[0] in ("a", "e", "i", "o", "u"):
        return ("Not a Valid String. Try again")
    else:
        return string.capitalize()
change_first_consonant("ave")
#print(change_first_consonant("ave"))

## 5.- Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip

def calculate_tip(tip_percentage, bill_total):
    if tip_percentage >= 0 and tip_percentage <= 1:
        return (tip_percentage * bill_total)
    elif tip_percentage > 1:
        return "You're an awesome tipper!"
    else:
        return "Not a valid tip amount: Either the service sucks, or you are a horrible tipper."

calculate_tip(2, 500)
#print(calculate_tip(2, 500))

## 6.- Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied

def apply_discount(original_price, discount_percentage):
    if original_price > 0:
        return (original_price - (original_price * (discount_percentage/100)))
    else:
        return "Wrong price"
#print(apply_discount(500, 30))

## 7.- Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output

def handle_commas(string):
    if "," in string:
        return string.replace(",", "")
    else:
        return int(string)
#print(handle_commas("3,000,000"))

## 8.- Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)

def get_letter_grade(grade):
    if grade >= 0 and grade < 1:
        return ("Your grade is: F")
    elif grade >= 1 and grade < 2:
        return ("Your grade is: D")
    elif grade >= 2 and grade < 3:
        return ("Your grade is: C")
    elif grade >= 3 and grade < 4:
        return ("Your grade is: B")
    elif grade >= 4 and grade <= 4.33:
        return ("Congratulations! Your grade is: A!")
    else:
        return "Ths is not a valid grade"

#print(get_letter_grade(3.95))

## 9.- Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed

def remove_vowels(string):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, "")
    return string
remove_vowels("perrito")
#print(remove_vowels("perrito"))

## 10.- Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(string):
    if string == ("100% Completed"):
        return string.strip("100%").lower()
    return string.lower().rstrip(" ").lstrip(" ").replace(" ", "_")
print(normalize_name("    EL PATRIARCADO DEBE CAER!!!   KLJSNDDF JNLiulenjna 38278347y24 @##@#E      "))




