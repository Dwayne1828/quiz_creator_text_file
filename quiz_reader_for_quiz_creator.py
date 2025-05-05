import tkinter as tk

class QuizReader:
    def __init__(self, file_name): 
        self.file_name = file_name #Initialize the file name
        
        self.question_no = 0
        
        self.questions = self.quiz_reader() #Call the quiz_reader method to read the quiz file
        self.print_quiz() #Call the print_quiz method to display the quiz questions
        self.checking_answer() #Call the checking_answer method to check the user's answer

    def quiz_reader(self): 
        with open(self.file_name, "r") as file:
            lines = file.readlines() #Stores the lines in a list 
    
            complete_questions = [] #Initialize an empty list to store the questions with answer and choices
            #Create a dictionary to store the questions, choices, and answers
            questions = {"question": "", "choices": [], "answer": None} #Initialize the dictionary with empty lists for choices and answer

            #Iterate through the lines to check for the presence of a question, choices, and answer
            for line in lines: 
                line = line.strip() #Removes leading and trailing whitespace
                
                if not line:
                    continue
                elif "Quiz Created" in line: #Checks if the line contains the word "Quiz Created"
                    continue #If it does, skip the line
                elif "Choice" in line: #Checks if the line contains the word "Choice"
                    questions["choices"].append(line) #Adds the choices into the choices list
                elif "Answer" in line: #Checks if the line contains the word "Answer"
                    questions["answer"] = line.split(": ")[1].strip()
                else: 
                    questions["question"] += " " + line #Accumulates the question text including the Question number

                if questions["question"] and questions["choices"] and questions["answer"]:    
                    complete_questions.append(questions) #Adds the question to the Questions list
                    questions = {"question": "", "choices": [], "answer": None} #Resets the dictionary for the next question

        if not complete_questions: #Checks if the list is empty
            print("⚠️ No valid questions found in the file.")
            return [] #Returns an empty list if no questions are found
        else:
            return complete_questions #Returns the list of questions with choices and answers        


    def print_quiz(self):
        if self.question_no < len(self.questions):  
            display_question = tk.Label(root, text=self.questions[self.question_no]["question"]) #Creates a label to display the quiz questions
            display_question.pack()

            self.question_no += 1 #Initialize the question number to 0


    def checking_answer(self):
        for question_no in self.quiz_reader():
            print(f"\n{question_no['question'].strip()}")
            for choice in question_no["choices"]:
                print(choice) 
            
            while True:
                user_answer = input("\nEnter your answer (a, b, c, d): ").strip().lower()

                if user_answer in ["a", "b", "c", "d"]:
                    if user_answer == question_no["answer"]:
                        print("✅ Correct!")
                    else:
                        print("❌ Incorrect!")
                    break
                else:
                    print("⚠️ Invalid input! Please enter a, b, c, or d.")

root = tk.Tk()
root.title("Quiz")
root.geometry("800x450")
quiz = QuizReader("Existingfile.txt")
root.mainloop()


