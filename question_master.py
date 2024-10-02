import csv
import os
import logging

# Setup logging
logging.basicConfig(filename='question_master.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class QuestionMaster:
    def __init__(self, csv_file='questions.csv'):
        self.csv_file = csv_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """ Load questions from the CSV file """
        try:
            if os.path.exists(self.csv_file):
                with open(self.csv_file, mode='r') as file:
                    reader = csv.DictReader(file)
                    self.questions = [row for row in reader]
            else:
                logging.warning(f"{self.csv_file} not found, starting with an empty question set.")
        except Exception as e:
            logging.error(f"Error loading questions: {e}")

    def save_questions(self):
        """ Save the current questions back to the CSV file """
        try:
            with open(self.csv_file, mode='w', newline='') as file:
                fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.questions)
        except Exception as e:
            logging.error(f"Error saving questions: {e}")

    def add_question(self, question, option1, option2, option3, option4, correct_option):
        """ Add a new question to the CSV """
        try:
            new_num = str(len(self.questions) + 1)
            self.questions.append({
                'num': new_num,
                'question': question,
                'option1': option1,
                'option2': option2,
                'option3': option3,
                'option4': option4,
                'correctoption': correct_option
            })
            self.save_questions()
            logging.info(f"Question {new_num} added successfully.")
        except Exception as e:
            logging.error(f"Error adding question: {e}")

    def search_question(self, question_num):
        """ Search a question by number """
        try:
            for question in self.questions:
                if question['num'] == question_num:
                    return question
            logging.warning(f"Question {question_num} not found.")
            return None
        except Exception as e:
            logging.error(f"Error searching question: {e}")

    def delete_question(self, question_num):
        """ Delete a question by number """
        try:
            self.questions = [q for q in self.questions if q['num'] != question_num]
            self.save_questions()
            logging.info(f"Question {question_num} deleted successfully.")
        except Exception as e:
            logging.error(f"Error deleting question: {e}")

    def modify_question(self, question_num, question, option1, option2, option3, option4, correct_option):
        """ Modify a question by number """
        try:
            for q in self.questions:
                if q['num'] == question_num:
                    q['question'] = question
                    q['option1'] = option1
                    q['option2'] = option2
                    q['option3'] = option3
                    q['option4'] = option4
                    q['correctoption'] = correct_option
                    self.save_questions()
                    logging.info(f"Question {question_num} modified successfully.")
                    return
            logging.warning(f"Question {question_num} not found.")
        except Exception as e:
            logging.error(f"Error modifying question: {e}")

    def display_questions(self):
        """ Display all the questions """
        if not self.questions:
            print("No questions available.")
        for q in self.questions:
            print(f"Q{q['num']}: {q['question']}")
            print(f"  1) {q['option1']}  2) {q['option2']}  3) {q['option3']}  4) {q['option4']}")
            print(f"Correct answer: {q['correctoption']}")
            print("-" * 50)

# Menu options for managing questions
def menu():
    qm = QuestionMaster()

    while True:
        print("\nQuestion Master Menu:")
        print("1. Add a question")
        print("2. Search for a question")
        print("3. Delete a question")
        print("4. Modify a question")
        print("5. Display all questions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            question = input("Enter the question: ")
            option1 = input("Option 1: ")
            option2 = input("Option 2: ")
            option3 = input("Option 3: ")
            option4 = input("Option 4: ")
            correct_option = input("Correct option (e.g., op1, op2): ")
            qm.add_question(question, option1, option2, option3, option4, correct_option)

        elif choice == '2':
            question_num = input("Enter question number: ")
            result = qm.search_question(question_num)
            if result:
                print(result)
            else:
                print("Question not found.")

        elif choice == '3':
            question_num = input("Enter question number to delete: ")
            qm.delete_question(question_num)

        elif choice == '4':
            question_num = input("Enter question number to modify: ")
            question = input("Enter the question: ")
            option1 = input("Option 1: ")
            option2 = input("Option 2: ")
            option3 = input("Option 3: ")
            option4 = input("Option 4: ")
            correct_option = input("Correct option (e.g., op1, op2): ")
            qm.modify_question(question_num, question, option1, option2, option3, option4, correct_option)

        elif choice == '5':
            qm.display_questions()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
