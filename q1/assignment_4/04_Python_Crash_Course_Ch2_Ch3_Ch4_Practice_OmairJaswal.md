**Name:** Omair Abid Jaswal

**Roll No:** PIAIC115285

# Assignment 04: Python Crash Course Practice (Chapters 2 - 4)

## Part 1: Variables & Input

### Q1. Favorite Movie Intro
* Ask the user for:
  * Their name
  * Their favorite movie
* Print a sentence like: `Ali’s favorite movie is Interstellar.`
```python
name = input("Please enter your name: ")
movie = input("Please enter your favorite movie name: ")

print(f"\n{name.strip().title()}'s favorite movie is {movie.strip().title()}")
```
### Q2. Case Converter
* Ask the user to enter a word.
* Print:
  * The word in uppercase
  * The word in lowercase
  * The word in title case

word = input("Please enter a word: ")

print(f"\nUppercase:", word.upper())
print(f"Lowercase:", word.lower())
print(f"Title case:", word.title())

### Q3. Simple Math with Input
* Ask the user to input two numbers using `input()`
* Convert them to `int` or `float`
* Print:
  * Sum
  * Difference
  * Product
  * Quotient
```
# Sample Output:
Enter first number: 5
Enter second number: 2

Sum: 7
Difference: 3
Product: 10
Quotient: 2.5
```
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSum:", int(num1 + num2))
print("Difference:", int(num1 - num2))
print("Product:", int(num1 * num2))
print("Quotient:", float(num1 / num2))
```
## Part 2: Lists & Indexing

### Q4. My Friends List
* Create a list of 4 friends’ names.
* Print each name using a `for` loop.
```python
friends = ["moiz hamid", "fahad afaq", "sohaib idrees", "hassan iqbal"]

print("My Friends List:")

for friend in friends:
  print(friend.strip().title())
```
### Q5. Update Your List
1. Create a list of 3 favorite fruits.
2. Replace the second fruit with another.
3. Add one fruit to the end using `.append()`.
4. Add one to the beginning using `.insert(0, ...)`.
5. Print the list after each change.
```python
fruits = ["apple", "banana", "orange"]
print("Original: ", fruits)

fruits[1] = "mango"
print("Replace: ", fruits)

fruits.append("grape")
print("Append: ", fruits)

fruits.insert(0, "banana")
print("Insert: ", fruits)
```
### Q6. List Length Reporter
1. Ask the user to enter 5 favorite animals (use `input()`).
2. Store each animal in a list.
3. After collecting:
  * Print the total number of animals using `len()`
  * Print the first and last animal using indexing
```python
animals = []
for i in range(5):
  animal = input(f"{i + 1}. Enter your favorite animal: ")
  animals.append(animal.strip())

print("\nTotal animals entered:", len(animals))
print("First animal:", animals[0].title())
print("Last animal:", animals[-1].title())
```
## For Loops & Ranges

### Q7. Print Numbers
Use `range()` and `for` loop to:
* Print numbers from 1 to 10
* Print even numbers from 2 to 20
* Print multiples of 5 from 5 to 50
```python
print("Numbers from 1 to 10")
for i in range(1, 11):
  print(i)

print("\nEven numbers from 2 to 20")
for i in range(2, 21, 2):
  print(i)

print("\nMultiples of 5 from 5 to 50")
for i in range(5, 51, 5):
  print(i)
```
### Q8. Squares Table
Use a `for` loop to print square numbers from 1 to 10:
```
1 squared is 1
2 squared is 4
3 squared is 9
...
10 squared is 100
```
```python
for i in range(1, 11):
  print(f"{i} squared is {i ** 2}")
```
## Part 4: List Comprehension & Slicing

### Q9. Make a List of Cubes
* Use list comprehension to generate cubes of numbers 1–5.
* Print the list.
```
# Output:
[1, 8, 27, 64, 125]
```
```python
cubes = [(i ** 3) for i in range(1, 6)]
print(cubes)
```
### Q10. Top 3 Movies
1. Ask the user to enter 5 movie names using `input()`.
2. Store them in a list.
3. Print:
  * The first 3 movies using slicing
  * The last 2 movies using slicing
```python
movies = []
for i in range(5):
  movies.append(input(f"{i + 1}. Please enter a movie name: "))

print("\nFirst 3 movies: ", movies[:3])
print("Last 2 movies: ", movies[-2:])
```
### Q11. Top Students
1. Ask the user to enter names of 5 students using `input()` (one by one).
2. Store the names in a list.
3. Then:
* Print a greeting for each student using a `for` loop.
* Print only the top 3 students using slicing.
* Copy the list using `[:]`, then:
* Add 2 new names to the copied list using `.append()`
* Print both the original and the new list to show that the original is unchanged.
```python
students = []
for i in range(5):
  students.append(input(f"Enter student name #{i + 1}: ").strip())

print("\n")

for student in students:
  print(f"Hello, {student.title()}")

print(f"Top 3 students:", students[:3])

print("\n")

copy = students[:]
copy.append(input(f"Enter another student name: ").strip())
copy.append(input(f"Enter one more student name: ").strip())

print("\nOriginal student list: ", students)
print("Copied student list: ", copy)
```
### Q12. Travel Wishlist
1. Create a list of 5 places you want to visit.
2. Print the original list.
3. Print a temporarily sorted list using `sorted()`.
4. Sort the list in reverse alphabetical order using `.sort(reverse=True)`.
5. Use `.reverse()` twice:
* First to flip and print the list
* Then to flip it back and print again
```python
places = ["China", "Russia", "Turkey", "Azerbijan", "Qatar"]
print("Original list:", places)

print("Temporarily sorted:", sorted(places))

places.sort(reverse=True)
print("Reverse alphabetical:", places)

places.reverse()
print("Reversed list:", places)

places.reverse()
print("Reversed again list:", places)
```
## Mini Challenge: Name Art Generator
Combine your understanding of input, lists, string slicing, for loops, and list length.

### Task:
1. Ask the user to enter their name.
2. Convert the name to a list of characters.
3. Print each character on a new line using a `for` loop.
4. Then print:
* The first 3 letters
* The last 2 letters
* The total number of letters using `len()`
```
J
a
h
a
n
z
a
i
b

First 3 letters: ['J', 'a', 'h']
Last 2 letters: ['i', 'b']
Total letters: 9
```
```python
name = input("Please enter your name: ").strip()
letters = list(name)

for letter in letters:
  print(letter)

print("\nFirst 3 letters:", letters[:3])
print("Last 2 letters:", letters[-2:])
print("Total letters:", len(letters))
```

