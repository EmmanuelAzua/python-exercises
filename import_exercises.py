### These are my first PYTHON "IMPORT" exercises

##  You will need to use imports to complete each exercise; in addition, these exercise will strengthen your problem solving and python coding skills

## You will be directed to create specific files in part 1, for the rest you may do your work in either import_exercises.py or import_exercises.ipynb

## 1.- Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
## a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
## b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result
## c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook

from function_exercises import normalize_name

from function_exercises import remove_vowels as vowel_slayer

import function_exercises
function_exercises.is_vowel("a")

from function_exercises import calculate_tip
calculate_tip(0.2, 350)

from function_exercises import get_letter_grade as grade
grade(70)

## Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in

## Read about and use the itertools module from the python standard library to help you solve the following problems:
## 2.- How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
## How many different combinations are there of 2 letters from "abcd"?
## How many different permutations are there of 2 letters from "abcd"?



