
# MCQ Based Online Exam Application

## Description

This project is an MCQ-based online exam application that allows participants to take exams by answering multiple-choice questions. The questions are stored in a CSV file (`questions.csv`), which can be managed using a Python script. The application consists of two main components:

1. **Question Master (`question_master.py`)**: This script manages the questions, allowing users to add, search, delete, modify, and display questions.
2. **Exam Client (`exam_client.py`)**: This script conducts the exam, displaying questions to the user and recording their answers.

## Features

- Load questions from a CSV file.
- Add, search, delete, and modify questions through a menu interface.
- Conduct an online exam and display results.
- Log actions to a log file (`question_master.log`).

## File Structure

```
/E:\Python project
├── question_master.py
├── exam_client.py
└── questions.csv
```

## Sample `questions.csv` Format

```csv
num,question,option1,option2,option3,option4,correctoption
1,10+20 ans is,op1=20,op2=30,op3=40,op4=10,op2
2,20-10 ans is,op1=20,op2=30,op3=40,op4=10,op4
3,2*2 ans is,op1=4,op2=5,op3=6,op4=7,op1
4,5/2 ans is,op1=2.5,op2=3,op3=6,op4=7,op1
5,capital of India,op1=delhi,op2=blr,op3=mum,op4=chn,op1
6,linux is a _____,op1=os,op2=app,op3=game,op4=antivirus,op1
```

## How to Use

1. **Setup**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/Sshafiqa/MCQ-based-online-exam-using-Python.git
   cd MCQ-based-online-exam-using-Python
   ```

2. **Add Questions**: Run `question_master.py` to manage your questions.

   ```bash
   python question_master.py
   ```

   Use the menu to add, modify, delete, or view questions.

3. **Take Exam**: Run `exam_client.py` to start the exam.

   ```bash
   python exam_client.py
   ```

   Follow the prompts to enter your name and university, then answer the questions.

## Sample Output

### Question Master Menu

When running `question_master.py`, the user will see the following menu:

```
Question Master Menu:
1. Add a question
2. Search for a question
3. Delete a question
4. Modify a question
5. Display all questions
6. Exit
Enter your choice: 
```

### Example of Conducting an Exam

When running `exam_client.py`, the output will look like this:

```
Exam started: 15/Sep/2024 12:46:30
Student: Venky, University: Cisco

Q1: 10+20 ans is
1) 20  2) 30  3) 40  4) 10
Enter your choice (op1, op2, op3, op4): op2

Q2: 20-10 ans is
1) 20  2) 30  3) 40  4) 10
Enter your choice (op1, op2, op3, op4): op4

...

Exam Completed!
Student Name: Venky
University  : Cisco
Marks scored: 2 out of 2
```

## Logging

All actions performed in `question_master.py` are logged in `question_master.log`. This log file records any errors or actions taken, providing a useful audit trail.


### Logging Output

All actions in `question_master.py` are logged in `question_master.log`. For example:

```
2024-09-15 12:46:30:INFO:Question 1 added successfully.
2024-09-15 12:46:35:WARNING:Question 2 not found.
2024-09-15 12:46:40:ERROR:Error modifying question: Question 3 not found.
```


## Workflow

### Diagram

```plaintext
                        +-------------------------+
                        |     Start Application    |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        |   Launch Question Master  |
                        +-------------------------+
                                   |
                                   v
                     +-----------------------------+
                     |        Main Menu Options     |
                     +-----------------------------+
                     |  1. Add a Question           |
                     |  2. Search for a Question    |
                     |  3. Delete a Question        |
                     |  4. Modify a Question        |
                     |  5. Display All Questions     |
                     |  6. Exit                     |
                     +-----------------------------+
                                   |
                                   v
                +------------------------------+
                |     Perform Selected Action   |
                +------------------------------+
                |  - Add/Modify/Delete/Search   |
                |  - Update questions.csv       |
                |  - Log actions in question_master.log |
                +------------------------------+
                                   |
                                   v
                        +-------------------------+
                        |   Return to Main Menu   |
                        +-------------------------+
                                   |
                                   v
                                (Exit)
                                   |
                                   v
                        +-------------------------+
                        |    Launch Exam Client    |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        |   Load Questions from    |
                        |       questions.csv      |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        |   Prompt for Student Info |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        |      Conduct Exam       |
                        +-------------------------+
                                   |
                                   v
                   +---------------------------------+
                   |   Display Questions & Collect    |
                   |           User Responses         |
                   +---------------------------------+
                                   |
                                   v
                        +-------------------------+
                        |   Calculate & Display    |
                        |      Results & Score     |
                        +-------------------------+
                                   |
                                   v
                                (End)
```

### Description

1. **Start Application**: The user starts the application, which can be either the Question Master or the Exam Client.

2. **Launch Question Master**: The user selects to manage questions by running `question_master.py`.

3. **Main Menu Options**: The application displays a menu with options to:
   - Add a Question
   - Search for a Question
   - Delete a Question
   - Modify a Question
   - Display All Questions
   - Exit

4. **Perform Selected Action**: Based on the user’s choice, the application performs the corresponding action:
   - **Add/Modify/Delete/Search**: Interacts with the nested data structure and updates `questions.csv`.
   - Logs actions in `question_master.log`.

5. **Return to Main Menu**: After completing the action, the user is returned to the main menu until they choose to exit.

6. **Launch Exam Client**: The user can then launch the exam client by running `exam_client.py`.

7. **Load Questions**: The exam client loads questions from `questions.csv`.

8. **Prompt for Student Info**: The user is prompted to enter their name and university.

9. **Conduct Exam**: The application displays the questions and collects responses from the user.

10. **Calculate & Display Results**: After answering all questions, the application calculates the score and displays the results.

11. **End**: The process concludes, and the user can choose to start over or exit.

## Requirements

- Python 3.x
- No external libraries are required (standard libraries used).

