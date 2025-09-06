# 🧪 Python Mini Projects Assignment

### 🗓️ Submission Deadline: 31-May-2025

### 🧑‍🏫 Instructor: Jahanzaib

---

## 📌 Objective

These three scenario-based projects will help you apply foundational Python concepts: variables, data types, conditionals, loops, and data structures (lists, tuples, sets, dictionaries). Each project is self-explanatory and designed to boost your problem-solving skills.

---

## 🔧 Submission Instructions

You may complete the assignment using **one of the following methods**:

### Option 1: Google Colab

- Build your assignment in **Google Colab**

### Option 2: Python Script Files

- Build each project as a separate `.py` file.
- Upload your `.py` files to a **GitHub repository**
- **Submit the GitHub repo link in Google Classroom**

### 📤 Assignment Submission Guidelines

Please follow these instructions carefully to submit your assignment:

1. ✅ **Complete All Questions**
   Make sure you attempt **all projects** from 1 to the 3

2. 💻 **Run Each Code Cell**
   Ensure that each code block is executed and displays the correct output.

3. 📝 **Use Meaningful Inputs**
   When prompted for input (e.g., name, movie, numbers), use realistic and clear values.

4. 📁 **Save and Share Google Colab Link**
5. 📩 **Submit to Google Classroom**

---

## 🔷 Project 1: Smart Grocery Store Assistant

### 📖 Scenario:

A grocery store wants a Python assistant to manage product inventory and generate purchase receipts.

### ✅ Requirements:

- Create a `product_catalog` dictionary: item name as key, and `(price, stock)` as value.
- Provide options to:
  - View available products
  - Add/update product stock or price
  - Simulate customer purchase (check stock, deduct quantity, calculate bill)
  - Generate bill with itemized prices and total
  - Print alerts for stock < 5

### 📚 Helping Tips:

- Use `input()` to take user actions
- Use `while True:` loop with an exit option
- Use functions for `display_products()`, `purchase_item()`, etc.

### 🧪 Sample Code Snippet:

```python
product_catalog = {
    "apple": (100, 10),
    "banana": (60, 20)
}

for product, (price, stock) in product_catalog.items():
    print(f"{product.capitalize()} - Rs.{price}, In stock: {stock}")
```

### ✅ Expected Output:

```
Welcome to the Smart Grocery Store Assistant
1. View Products
2. Add/Update Product
3. Purchase Items
4. Exit
Enter your choice: 1
Apple - Rs.100, In stock: 10
Banana - Rs.60, In stock: 20
```

---

## 🔷 Project 2: Library Book Management System

### 📖 Scenario:

Build a simple library system where users can borrow, return, or view books.

### ✅ Requirements:

- Store books in a dictionary:

```python
books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True}
}
```

- Menu Options:
  - View all books
  - Borrow a book (check if available)
  - Return a book
  - Add a new book
  - View borrowed books

### 📚 Helping Tips:

- Use `.lower()` for case-insensitive match
- Track borrowed books using a list or dictionary

### 🧪 Sample Code Snippet:

```python
if books[book_title]["available"]:
    books[book_title]["available"] = False
    borrowed.append(book_title)
```

### ✅ Expected Output:

```
Welcome to the Library System
1. View Books
2. Borrow Book
3. Return Book
Enter choice: 2
Enter book name: 1984
You have borrowed "1984".
```

---

## 🔷 Project 3: Student Report Card Generator

### 📖 Scenario:

Create a system that accepts marks for 5 subjects and generates a report card.

### ✅ Requirements:

- Input: student name, roll number, and marks for 5 subjects
- Store data like:

```python
students = {
    "Ali": {
        "roll": 101,
        "marks": [80, 90, 85, 88, 92]
    }
}
```

- Calculate total, average, and grade (A, B, C, D, F)
- Allow multiple student entries

### 📚 Helping Tips:

- Use `sum()` and `len()` to calculate average
- Use if-else ladder for grading

### 🧪 Sample Code Snippet:

```python
average = sum(marks) / len(marks)
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
...
```

### ✅ Expected Output:

```
Student Name: Ali
Roll No: 101
Marks: [80, 90, 85, 88, 92]
Total: 435
Average: 87.0
Grade: B
```

---

## 🎮 Bonus Project: Mini Quiz Game

### 📖 Scenario:

Build a fun Python quiz game that asks 5 questions to the user and scores them.

### ✅ Requirements:

- Store questions in a dictionary or list
- Ask each question using `input()`
- Count the number of correct answers
- Show final score and feedback

### 📚 Helping Tips:

- Use a list of tuples or dictionaries to store question-answer pairs
- Use a `for` loop to iterate through questions

### ✅ Expected Output:

```
Q1: What is the capital of France?
Your Answer: Paris
Correct!

Final Score: 5/5
Excellent job!
```

---

**Good luck and happy coding! 🎉**

