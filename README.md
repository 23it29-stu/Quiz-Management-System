# 🎯 Quiz Management System

A desktop-based **Quiz Management System** developed using **Python, CustomTkinter, and MySQL**. The application allows users to create quizzes, attempt multiple-choice questions with a countdown timer, view their score instantly, review their answers, and store all quiz results in a MySQL database.

This project was developed as part of an internship to demonstrate Python GUI development, database integration, and object-oriented programming concepts.

---

# 📌 Project Features

## 📝 Create Quiz
- Create unlimited quizzes
- Add unlimited multiple-choice questions
- Set quiz name and category
- Add quiz description
- Select difficulty level (Easy, Medium, Hard)
- Set custom time limit for each quiz
- Set passing percentage
- Automatically stores total number of questions
- Questions are saved into the MySQL database

---

## 🎮 Take Quiz
- Select any available quiz
- Enter student name before starting
- Displays quiz timer
- Previous and Next navigation
- Questions can be skipped
- Selected answers are remembered while navigating
- Manual quiz submission
- Automatic submission when timer reaches zero

---

## 📊 Result System
Immediately after submitting the quiz, the application displays:

- Student Name
- Quiz Name
- Total Questions
- Correct Answers
- Wrong Answers
- Final Score
- Percentage
- Pass / Fail Status
- Time Taken

The quiz window automatically closes and the result window opens after submission.

---

## ✅ Review Answers
Users can review every attempted question after viewing the result.

For each question, the application displays:

- Question
- All four options
- Selected answer
- Correct answer
- Correct / Incorrect status

This helps users understand their mistakes.

---

## 💾 Result Management
Every quiz attempt is automatically stored in the MySQL database.

Stored information includes:

- Student Name
- Quiz ID
- Score
- Percentage
- Pass / Fail Status
- Time Taken
- Date and Time of Attempt

---

## 🔍 Search and Filter
The application supports:

- Viewing quizzes category-wise

---

# 🛠 Technologies Used

- Python 3
- CustomTkinter
- MySQL
- mysql-connector-python

---
---

# 🗄 Database

The application uses MySQL with the following tables:

### Quiz Table

Stores quiz information such as

- Quiz Name
- Category
- Description
- Difficulty
- Time Limit
- Passing Percentage
- Total Questions

---

### Questions Table

Stores

- Question
- Option A
- Option B
- Option C
- Option D
- Correct Answer

---

### Results Table

Stores

- Student Name
- Quiz ID
- Score
- Percentage
- Status
- Time Taken
- Attempt Date & Time

---

# 🚀 Installation

### Step 1

Clone the repository

```bash
git clone <repository-link>
```

---

### Step 2

Install required packages

```bash
pip install -r requirements.txt
```

---

### Step 3

Create a MySQL database

```sql
CREATE DATABASE quiz_management;
```

---

### Step 4

Create the required database tables (`quiz`, `questions`, and `results`) and import your SQL schema.

---

### Step 5

Update your database credentials inside `database.py`

```python
host="localhost"
user="your_username"
password="your_password"
database="quiz_management"
```

---

### Step 6

Run the application

```bash
python main.py
```

---

# 🖥 Application Workflow

### 1. Create Quiz

- Enter quiz details
- Add questions
- Save the quiz

↓

### 2. Take Quiz

- Select quiz
- Enter student name
- Attempt questions
- Navigate using Previous and Next
- Submit manually or wait for automatic submission

↓

### 3. Result

The application immediately displays

- Score
- Percentage
- Pass / Fail
- Time Taken

↓

### 4. Review Answers

Users can compare their answers with the correct answers question by question.

↓

### 5. View Previous Results

Previously attempted quiz results can be viewed from the application.

---

# ✨ Key Functionalities

✔ Create Multiple Quizzes

✔ Unlimited Questions

✔ Timer for Each Quiz

✔ Automatic Quiz Submission

✔ Previous & Next Navigation

✔ Skip Questions

✔ Manual Submission

✔ Instant Result Generation

✔ Pass / Fail Evaluation

✔ Answer Review

✔ MySQL Database Integration

✔ Result History


---

# 📚 Concepts Used

This project demonstrates:

- Python Programming
- Object-Oriented Programming (OOP)
- GUI Development using CustomTkinter
- MySQL Database Connectivity
- CRUD Operations
- Timer Implementation
- Result Processing
- Desktop Application Development

---



# 🔮 Future Enhancements

Possible future improvements include:

- User Authentication
- Admin Panel
- Leaderboard
- Randomized Questions
- Negative Marking
- Image-Based Questions
- PDF Result Export
- Dark Mode




