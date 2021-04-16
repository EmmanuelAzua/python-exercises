### This is my first PYTHON assessment

# Grading
# Your assessment will be graded based on the examples given.
# One point will be awarded for each problem that is correctly solved.
# Each problem includes sample output from an interactive Python session (i.e. running the python command from your terminal).
# If the examples for each problem can be run, and the correct output produced, you will receive credit for the problem.
# No partial credit will be awarded, and no credit is given if the function is misnamed, or if the function does not run (i.e. it produces an error when we try to run it).

# 1.- Write a function named isnegative. It should accept a number and return a boolean value based on whether the input is negative

def isnegative(number):
    if number < 0:
        return True
    else:
        return False
print(isnegative(number))

# 2.- Write a function named count_evens. It should accept a list and return the number of even numbers in the list

def count_evens(num_range):
    return even_numbers = [num for num in range(num_range) if num % 2 == 0]
#num_range = 10
print(even_numbers)
print(len(even_numbers))

# 3.- Write a function named increment_odds. It should accept a list of numbers and return a new list with the odd numbers from the original list incremented

def increment_odds(numbers):
    odd_numbers = []
    for number in numbers [number % 2 != 0]:
         return odd_numbers.append()
    oddnum_plusone = []
    for num in odd_numbers [num + 1]:
        return oddnum_plusone.append()
    
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_numbers)
print(oddnum_plusone)

# 4.- Write a function named average. It should accept a list of numbers and return the mean of the numbers

def average(list): 
    result = sum(list) / len(list) 
    return result 

#list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(average(list))

# 5.- Create a function named name_to_dict. It should accept a string that is a first name and last name separated by a space, and return a dictionary with first_name and last_name keys.

def name_to_dict(string):
    first_last_name = string.split()
    name = first_last_name[0]
    last_name = first_last_name[1]
    full_name = {}
    full_name["name"] = name
    full_name["last name"] = last_name
    return string.replace(" ", "_")
#string = "Emmanuel Rivera"
print(name_to_dict(string))

# 6.- Write a function named capitalize_names. It should accept a list of dictionaries where each dictionary represents a person and has keys first_name and last_name.
# It should return a list of dictionaries with each person's name capitalized.

def capitalize_names():


# 7.- Write a function named count_vowels. It should accept a word and return a number that is the number of vowels in the given word. "y" should not count as a vowel.

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in word if i in vowels])

print(count_vowels(word))

# 8.- Write a function named analyze_word.
# It should accept a string that is a word and return a dictionary with information about the word: the total number of characters in the word, the original word, and the number of vowels in the word.

def analyze_word(word):
    word_details = {}
    word_details["number of characters"] = number_of_characters
    word_details["original word"] = original_word(word)
    word_details["number of vowels in word"] = number_of_vowels
    number_of_characters = word_details[0]
    original_word = word_details[1]
    number_of_vowels = word_details[2]
    (return len([char for char in word]))
    print(len([char for char in word]))
    return word
    print (word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in word if i in vowels])
    print(len([i for i in word if i in vowels]))

word = "word"

#string = "Emmanuel Rivera"
print(analyze_word(word))






