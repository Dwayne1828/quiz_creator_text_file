import os 
from datetime import datetime

def file_maker(): 
    while True:   
        file_name = input("Enter the file name for your quiz: ").strip()
        #Check if the file name ends with .txt, if not add it
        if file_name.endswith(".txt"):
            file_name = file_name
        else:
            file_name = file_name + ".txt"

        #Check if the file already exists, if it does ask the user if they want to edit it or create a new one
        if os.path.exists(file_name): 
            edit = input("File already exists. Do you wish to edit the file? (yes/no): ")
            if edit.lower().strip() == "yes": 
                return file_name
            elif edit.lower().strip() == "no": 
                continue
        else: 
            return file_name

def question_checker(file_name):
    #Check if the file exists, if not return 0
    if not os.path.exists(file_name): 
        return 1
    
    with open(file_name, "r") as quiz_file: 
        lines = quiz_file.readlines()
        for line in reversed(lines):
            if line.startswith("Question"):
                #Get the question number from the line
                question_number = int(lines.split()[1].strip(":"))
                return question_number + 1 #Return the next question number

#Function to asks the user for questions and answers and writes them to the file
def create_quiz():
    #Get the file name from the user
    file_name = file_maker()

    #Open the file in append mode to create if exists or create a new one
    with open(file_name, "a") as quiz_file:
        #Get the current date and time
        now = datetime.now()
        current_time_date = now.strftime("%m/%d/%Y %H:%M:%S")

        quiz_file.write(f"Quiz Created - {current_time_date}\n")
        quiz_file.write("\n")

        #Starts the Question number at 1
        question_number = int(question_checker(file_name))

        #While true for a loop to allow the user to decide when to stop entering questions
        while True: 
            question = input("Enter a question: ") 
            quiz_file.write(f"Question {question_number}: {question}\n") 
            question_number += 1

            #Ask the user for choices 
            for option in ["a", "b", "c", "d"]: 
                choice = input(f"Enter choice {option}: ")
                quiz_file.write(f"Choice {option}: {choice}\n")
                
            #Ask the user for the correct answer
            answer = input("Enter the correct answer (a, b, c, d): ")
            quiz_file.write(f"Answer: {answer}\n")
            quiz_file.write("\n")
        
            #Ask the user if they want to add another question
            another = input("Do you want to add another question? (yes/no): ")
            if another.lower().strip() != "yes":
                break

create_quiz()

