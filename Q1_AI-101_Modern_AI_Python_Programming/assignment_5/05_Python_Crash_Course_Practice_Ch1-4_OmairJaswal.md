**Name:** Omair Abid Jaswal

**Roll No:** PIAIC115285

# Assignment 05: Python Crash Course Practice (Chapters 1 - 4)

### Q1. Palindrome Check
* Write a program that takes a string input from the user and prints whether it is a palindrome (a string that reads the same forwards and backwards). Test the code with two cases one where the input string is a palindrome and the other where it is not a palindrome.


# Run code twice
for i in range(0, 2):
  # Get user input
  text = str(input("Enter a word: ")).strip()

  # Sanitise input
  word = text.lower()

  # Prepare two output cases
  outputs = (text + " is not a palindrome", text + " is a palindrome")

  # Print output
  print(outputs[word == word[::-1]])
  print()

### Q2. Formatted Table
* Create a list of tuples where each tuple contains an item name (string) and its price (float). First print the list and then Use a for loop to print each item and its price along with serial number, aligned using the tab escape character.

# List of tuples containing Name and Price
items = [
    ("Apples", 1.25),
    ("Bananas", 0.75),
    ("Oranges", 2.50)
]

# Print items list
print("Items list:", items)
print()

# Print nicely formatted items list
print(f"#\tItem\t\tPrice")
for i in range(len(items)):
  print(f"{i + 1}\t{items[i][0]}\t\t{items[i][1]}")

### Q3. Vowel Counter
* Given a string sentence, write a program that counts and print how many vowels it contains.
  * Print the original string
  * Print the count of vowels

# Initialise variables
vowels = "aeiou"
vowels_found = []

# Get sentence from user
# sentence = str("The quick brown fox jumps Over the lazy dog.").strip()
sentence = str(input("Enter a sentence: ")).strip()

# Check for all vowels in the sentence
# Loop through all the letters in the sentence
# Lowercase entire sentence to strictly match with vowels variable
for letter in sentence.lower():
  # Check if letter exists in vowels list, return Boolean
  # Multiply the Boolean result with the single letter list
  # If True = 1, then vowel variable is set with the letter
  # If False = 0, then the vowel variable is empty
  vowel = [letter] * (letter in vowels)

  # Add the vowel variable into the running vowels_found list
  vowels_found = vowels_found + vowel

# Print outputs
print("\nSentence:\n", sentence)
print("\nNumber of vowels found:", len(vowels_found))
# print("Vowels found:", vowels_found)

### Q4. Discount Calculator
* You have a list of product prices (floats), e.g. [19.99, 5.50, 100.0]. Apply a 15% discount to each price and store the new prices in a separate list. Then print original list, discounted list and each original and discounted price side by side.

# Initialise product price lists
prices = [19.99, 5.50, 100.0]
discounts = []
discounted_prices = []

# Process discount
percent_discount = 15
discount = percent_discount / 100

# Apply dicount on all products in list
for price in prices:
  discounted_amount = price * discount
  discounts.append(discounted_amount)
  discounted_prices.append(price - discounted_amount)

# Print output
print("Original prices:", prices)
# print("Discounts:", discounts)
print("Discounted prices:", discounted_prices)

# Nicely formatted output
# print(f"\nPrice\tDiscount\tDiscounted Price")
print(f"\nOriginal Price\tDiscounted Price")
for i in range(len(prices)):
  # print(f"{prices[i]}\t{discounts[i]}\t{discounted_prices[i]}")
  print(f"{prices[i]}\t\t{discounted_prices[i]}")

### Q5. Phone Number Formatter
* You have a list of 11-digit strings like ["03123456789", "03001234567"]. Convert each into the format "+92-XXX-XXXXXXX" and print them. Print Original and Formatted number side by side.

# Initialise variables
numbers = ["03123456789", "03001234567"]
formatted = []

# Format all phone numbers
for num in numbers:
  formatted.append("+92-" + num[1:4] + "-" + num[4:])

# Formatted output
print("Original\tFormatted")
for i in range(len(numbers)):
  print(f"{numbers[i]}\t{formatted[i]}")

### Q6. Score Statistics
* You have a tuple of exam scores, e.g. (72, 85, 91, 58, 76).
  * Print the provided tuple
  * Convert it to a list and print it.
  * Compute and print the minimum, maximum, and average score.

# Initialise exam scores tuple
scores = (72, 85, 91, 58, 76)
print("Original Tuple:", scores)

# Convert tuple to list
score_list = list(scores)
print("Converted List:", score_list)

# Compute average score
total = 0
for score in score_list:
  total += score
average = total / len(score_list)

# Print results
print("\nMinimum Score:", min(score_list))
print("Maximum Score:", max(score_list))
print("Average Score:", average)

### Q7. Reverse Each Word in a Sentence
* Given a sentence string, reverse each word individually but keep the word order.
  * Print the original sentence
  * Print the formatted sentence

# Initialise variables
sentence = str("Python is a great language!").strip()
word = ""
reversed_sentence = ""

# Manually split sentence into a list of words
for letter in sentence:
  is_space = (letter == " ") * 1 # returns 1 if space, 0 if not space
  word = word + (letter * (1 - is_space)) # Build the word if no space
  reversed_sentence += (word[::-1] * is_space) + (letter * is_space) # Add the reversed word and space if current character is a space
  word = word * (1 - is_space) # Clear word variable if space

# Print results
print("Original Sentence:\n", sentence)
print()
print("Reversed Sentence:\n", reversed_sentence.strip())

### Q8. Running Sum List
* From a given list create a list where each element is the sum of all previous elements (inclusive). Print both the lists.

# Initialise variables
numbers = [1, 2, 3, 4, 5]
running_sum = []
total = 0

# Compute total and running sum
for number in numbers:
  total += number
  running_sum.append(total)

# Print results
print("Original list:", numbers)
print("Running sum list:", running_sum)

### Q9. Interleave Two Lists
* Combine two equal-length lists into a single one by alternating elements.
  * Input: [1, 2, 3] and ['a', 'b', 'c']
  * Output: [1, 'a', 2, 'b', 3, 'c']
* Print all three lists.

# Initialise variables
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]

interleaved = []

# Interleave the list
for i in range(len(list_1)):
  interleaved.append(list_1[i])
  interleaved.append(list_2[i])

# Print result
print("List 1:", list_1)
print("List 2:", list_2)
print("Interleaved list:", interleaved)

### Q10. Repeat Letters
* Given a string, return a new string where each letter is repeated twice. Print both the strings

# Initialise variables
# text = str("Hello World").strip()
text = str(input("Enter some text: ")).strip()
doubled = ""

# Double up
for character in text:
  # Multipling character by 2 to duplicates it 2 times
  doubled += character * 2

# Print result
print("\nOriginal:", text)
print("Doubled:", doubled)