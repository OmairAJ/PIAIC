# Assignment 03: Python Crash Course Practice (Chapters 2 & 3)


## Chapter 2: Variables and Simple Data Types (15 Questions)

### Basic

1. Create a variable called `greeting` and store any message. Print it.
```python
# Initialise a string variable named 'greeting' and set it's value with some text inside quotes
greeting = "Hello World!"

# Print variable 'greeting' on screen
print(greeting)
```

2. Change the value of `greeting` to a new message. Print the updated message.
```python
#  Update the 'greeting' string variable with some new text
greeting = "Hello Pakistan!"

# Print the output
print(greeting)
```

3. Create two variables `first_name` and `last_name`. Combine them into a full name using an f-string.
```python
# Create two new string variables
first_name = "Omair"
last_name = "Jaswal"

# Combine both string variables togather into one variable
full_name = f"{first_name} {last_name}"

# Print the final result
print(full_name)
```

4. Print a quote along with the author's name using an f-string.
```python
# Initialise string variable with quote and author
quote = "To err is human. To really screw things up requires a computer."
author = "Murphy’s Laws"

# Combine and format the quotation
# New line (\n) and Double Quotes (\") added by using Python's Escape Sequence
quotation = f"According to {author}:\n\"{quote}\""

# Print the formatted output
print (quotation)
```

5. Store a person's name with extra spaces. Strip the spaces before printing.
```python
# Badly entered person name
f_name = "         OmAir  "
l_name = "    jaswal"

# Clean and formatted final name
name = f"{f_name.strip()} {l_name.strip()}"

# Print proper name output
print(name.title())
```


### Intermediate

6. Take a number, add 5, multiply by 2, subtract 3, and print the final result.
```python
# Initialise integer variable with some number
number = 2

# With the number, Add 5, multiply by 2 and subtract 3
# The PEMDAS order of operations will be applied here
# Parentheses: Expressions within parentheses are evaluated first.
# Exponents: Exponentiation operations are performed next.
# Multiplication and Division: These are performed from left to right.
# Addition and Subtraction: These are performed last, also from left to right.
number = ((number + 5) * 2) - 3

# Print final result
print(number)
```

7. Create two numbers `a` and `b` and print their sum, difference, product, and quotient.
```python
# Initialise two integer variables with some numbers
a = 2
b = 3

# Process numbers
sum = a + b
difference = a - b
product = a * b
quotient = a / b

# Print nicely formatted results
print("Sum:\t\t", a, "+", b, "=", sum)
print("Difference:\t", a, "-", b, "=", difference)
print("Product:\t", a, "*", b, "=", product)
print("Quotient:\t", a, "/", b, "=", quotient)
```

8. Find the square and cube of a number using the `**` operator.
```python
# Initialise integer variable with some number
number = 2

# Process square and cube of number
square = number ** 2
cube = number ** 3

# Print final result
print("Square of", number, "=", square)
print("Cube of", number, "=", cube)
```

9. Print the sum of three floating-point numbers.
```python
# Initialise three float variables with some numbers
pi = 3.14159
e = 2.71828
phi = 1.61803

# Sum of all floating-point numbers
sum = pi + e + phi

# Print final result
print("Pi\t", pi)
print("e\t", e)
print("Phi\t", phi)
print("\t -------")
print("SUM\t", sum)
```

10. Assign three variables `x, y, z` in a single line and print them.
```python
# Initialise three variables in a single line
x, y, z = 1, 2, 3

# Print result
print(x, y, z)
```


## Chapter 3: Introducing Lists (15 Questions)

### Basic

11. Create a list of 5 favorite fruits and print each fruit separately.
```python
# Initialise list variable with five fruits
fruits = ["mango", "banana", "orange", "lychee", "water melon"]

# Print list
print("Fruits List:\t", fruits)
```

12. Modify the second item in the list and print the updated list.
```python
# Update second item in fruits list with another fruit
fruits[1] = "apricot"

# Print updated list
print("Updated Fruits List:\t", fruits)
```

13. Append a new fruit and insert another at the beginning of the list.
```python
# Add a new fruit at the end of the list
fruits.append("papaya")

# Print updated list
print("Append new fruit in list:\t", fruits)


# Add a new fruit at begining of the list
fruits.insert(0, "peach")

# Print updated list
print("Insert new fruit in list:\t", fruits)
```

14. Demonstrate deleting an item using del, pop(), and remove().
```python
# Removed 3rd fruit from the list
del fruits[2]
# Print updated list
print("Delete 3rd fruit from list:\t\t", fruits)


# Remove last fruit from the list
popped_fruit = fruits.pop()

# Print updated list
print("Popped fruit from list:\t\t\t", fruits)
print("Popped fruit:\t\t\t\t", popped_fruit)


# Remove specific fruit from the list
fruits.remove("lychee")

# Print updated list
print("Removed Lychee fruit from list:\t", fruits)
```

15. Sort the list permanently with sort() and temporarily with sorted(). Print before and after each.
```python
# Temorarily sort the original fruits list
print("Current fruits list:\t\t", fruits)
print("Temporarily sorted list:\t", sorted(fruits))
print("Current fruits list:\t\t", fruits, "\n")


# Permanently sort the fruits list
print("Current fruits list:\t\t", fruits)
fruits.sort()
print("Permanently sorted list\t\t", fruits)
print("Current fruits list:\t\t", fruits)
```


### Intermediate

16. Create a list of dream travel destinations:
* Sort alphabetically
* Reverse the order
* Find the total number of destinations
```python
# Initialise dream travel destinations list variable
destinations = ["Italy", "Turkey", "United Arab Emirates", "Thailand", "Greece", "Malaysia", "Saudia Arabia", "Maldives", "Spain", "Qatar"]

# Sort destinations alphabetically in reverse order
destinations.sort(reverse=True)

# Print results
print("There are total", len(destinations), "dreams destination in the list.")
print("These dream travel destinations are: ", destinations)
```

17. Start with an empty guest list:
* Append three guests
* Insert a guest at the beginning
* Remove one guest with pop()
* Print the final invitation list
```python
# Initialise 'guests' variable
guests = []

# Print new guest list
print(f"New Guest list:\t\t{guests}")

# Append three guests
guests.append("Moiz Hamid")
guests.append("Swaleh Qayum")
guests.append("Fahad Afaq")

# Print updated guest list
print(f"Updated guest list:\t{guests}")

# Insert one guest at the begining
guests.insert(0, "Sohaib Idrees")

# Print edited guest list
print(f"Edited guest list:\t{guests}")

# Remove one guest from the end
guests.pop()

# Print final invitation list
print(f"Final invitation list:\t{guests}")
```

18. Access the last three elements of a list without using negative indices.
```python
# Initialise list
cars = ["honda", "toyota", "suzuki", "hyundai", "audi", "tesla"]

# Print current list
print(f"Current list:\t\t\t{cars}")

# Length of cars list
length = len(cars)

# Print length of list
print(f"List size:\t\t\t{length}")

# Last three elements from the list
# Avoiding use of negative indices by utilising Python's Slice syntax.
# We give the Index Start & End, and Python itself increments one step forward.
# Start Index is list Length - 3, which comes out as 3
# End Index can be set to Length or left empty for Python to automatically set.
# Adding the colon (:) after the Start Index is required.
last_three = cars[length-3:]

# Print output
print(f"Last three cars in the list:\t{last_three}")
```

19. Print only the even numbers from a list.
```python
# Initialise list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
# Utilising Python's Slice syntax, but with Step this time.
# Index Start from 1, End is omitted and we increment two step forward.
# Start Index is set to 1, which is begining of the list.
# End Index is not set, which defaults to list's last element automatically.
# Step is set to jump 2 positions each time.
# Both colon's (:) must be added in middle for correct syntax.
evens = numbers[1::2]

# Print final output
print(f"List of numbers:\t{numbers}")
print(f"Even numbers from list:\t{evens}")

# This simple method works for sorted natural numbers in sequence only
# For advance retrival of even numbers, we will need to utilise syntax and methods not covered in Chapters 2 and 3.
```

20. Print the squares of the first 10 natural numbers using a list.
```python
# Initialise list of natural numbers
natural = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Set multiple variables with natural numbers list
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = natural[:12]

# Calculate squares of all natural numbers
squares = [
    n1 ** 2,
    n2 ** 2,
    n3 ** 2,
    n4 ** 2,
    n5 ** 2,
    n6 ** 2,
    n7 ** 2,
    n8 ** 2,
    n9 ** 2,
    n10 ** 2,
    n11 ** 2,
    n12 ** 2
           ]

# Print result
print(squares[:10])
```


## Bonus Challenge

* Combine variables and lists:
  * Ask the user for five favorite movies.
  * Store them in a list.
  * Print the sorted list alphabetically.
```python
# Set variables with user's favorite movies
m1 = "inception "
m2 = "Interstellar      "
m3 = "The dark kNight"
m4 = "  Her"
m5 = "man   of                   steel"
# or Get user's favorite movies using input() into variables
# m1 = input(f"Enter your favorite movie #1: ")
# m2 = input(f"Enter your favorite movie #2: ")
# m3 = input(f"Enter your favorite movie #3: ")
# m4 = input(f"Enter your favorite movie #4: ")
# m5 = input(f"Enter your favorite movie #5: ")

# Build a clean users favorite movies list
# Used strip() to remove trailing white space from both left and right sides
# Used replace() to remove double spaces between words
# Used title() to Capitilise the words
movies = [
    m1.strip().replace("  ", "").title(),
    m2.strip().replace("  ", "").title(),
    m3.strip().replace("  ", "").title(),
    m4.strip().replace("  ", "").title(),
    m5.strip().replace("  ", "").title()
]

# Sort the movies list without affecting the original list
sorted_movies = sorted(movies)

# Print nicely formatted output
print(
    "\n\nYour favorite movies in alphabetical order:\n"
    f"1. {sorted_movies[0]}\n"
    f"2. {sorted_movies[1]}\n"
    f"3. {sorted_movies[2]}\n"
    f"4. {sorted_movies[3]}\n"
    f"5. {sorted_movies[4]}\n"
)
```

