# This is my first PYTHON independent practice exercise file

99.9
type(99.9)

type(False)

### What data type would best represent:

# A term or phrase typed into a search box?                          R.- String
# If a user is logged in?                                            R.- Boolean
# A discount amount to apply to a user's shopping cart?              R.- Float
# Whether or not a coupon code is valid?                             R.- Boolean
# An email address typed into a registration form?                   R.- String
# The price of a product?                                            R.- Float
# A Matrix?                                                          R.- List
# The email addresses collected from a registration form?            R.- Dictionary
# Information about applicants to Codeup's data science program?     R.- Dictionary



### For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL

# 1. Error
# 2. 2
# 3. Int
# 4. none
# 5. Error
# 6. False
# 7. False
# 8. False
# 9. True
# 10. Error
# 11. 1
# 12. False
# 13. False
# 14. Error, syntax
# 15. True
# 16. True
# 17. Error, concat
# 18. [1 , 2]
# 19. [1 , 1]
# 20. Error, can't multiply sequence by non-int of type 'list'
# 21. True
# 22. TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


### Create a Python script file named data_types_and_variables.py.
# Inside it, write some Python code, that is, variables and operators, to describe the following scenarios.
# Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code

# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

The_Little_Mermaid = a = 1
Brother_Bear = b = 1
Hercules = c = 1
dayrent = 3
Total_Rent = dayrent * (3 * a + 5 * b + c)
print(Total_Rent)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

Google = a = 400
Amazon = b = 380
Facebook = c = 350
This_Week_Check = (10 * c + 6 * a + 4 * a)
print(This_Week_Check)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule

full_class = True
schedule_conflict = True
Enrolled_Student = (full_class and schedule_conflict)
print(Enrolled_Student)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

Buys_more_than_2 = True
Not_expired = False
Premium_member = True
Product_offer = (Buys_more_than_2 and Not_expired) or (Premium_member and Not_expired)
print(Product_offer)

# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'
len(password) > 4
len(username) < 21
password != username
password.startswith != " " and password.endswith != " "
username.startswith != " " and username.endswith != " "