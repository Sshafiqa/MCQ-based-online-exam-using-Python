import csv
import os
from datetime import datetime

class ExamClient:
    def __init__(self, csv_file='questions.csv'):
        self.csv_file = csv_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """ Load questions from the CSV file """
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.questions = [row for row in reader]

    def conduct_exam(self):
        """ Conduct the exam by asking questions to the user """
        if not self.questions:
            print("No questions available for the exam.")
            return

        student_name = input("Enter student name: ")
        university = input("Enter university: ")
        score = 0

        print(f"\nExam started: {datetime.now().strftime('%d/%b/%Y %H:%M:%S')}")
        print(f"Student: {student_name}, University: {university}\n")

        for q in self.questions:
            print(f"Q{q['num']}: {q['question']}")
            print(f"1) {q['option1']}  2) {q['option2']}  3) {q['option3']}  4) {q['option4']}")
            user_choice = input("Enter your choice (op1, op2, op3, op4): ")

            if user_choice == q['correctoption']:
                score += 1

        # Display results
        print(f"\nExam Completed!")
        print(f"Student Name: {student_name}")
        print(f"University  : {university}")
        print(f"Marks scored: {score} out of {len(self.questions)}")

if __name__ == "__main__":
    ec = ExamClient()
    ec.conduct_exam()
