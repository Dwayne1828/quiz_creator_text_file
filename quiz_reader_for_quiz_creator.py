import tkinter as tk
from tkinter import messagebox

class QuizReader:
    def __init__(self, file_name): 
        self.file_name = file_name #Initialize the file name
        
        self.root = tk.Tk()
        
        self.choosed_answer = tk.IntVar()
        self.question_no = 0
        self.correct_ans = 0
        self.wrong_ans = 0
        self.questions = self.quiz_reader() #Calls the quiz_reader method to read the quiz file and store the questions

        self.display_question = tk.Label(self.root, text="Start") #Creates a label to display the quiz questions
        self.display_question.place(relx=0.5, rely=0.4, anchor="center")
        self.display_question.config(font=("Arial", 16), wraplength=700) #Sets the font and wrap length for the label
        
        self.next_button = tk.Button(self.root, text="Let's Go!", command=self.next_question) #Creates a button to navigate to the next question
        self.next_button.place(relx=0.5, rely=0.6, anchor="center")
        self.next_button.config(font=("Arial", 10), width=10, height=2) #Sets the font, width, and height for the button

        
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
            messagebox.showinfo("⚠️ No valid questions found in the file.")
            return [] #Returns an empty list if no questions are found
        else:
            return complete_questions #Returns the list of questions with choices and answers        


    def next_question(self):
        if self.question_no < len(self.questions):   
            self.next_button.config(text="Next", command=self.current_check_answer) #Changes the button text to "Next"
            self.next_button.place(relx=0.5, rely=0.7, anchor="center") #Places the button in the center of the window
            self.radio_btn = self.choices_radio_btn()
            self.options_question_no()
            self.display_question.config(text=self.questions[self.question_no]["question"].strip()) 
            self.display_question.place(relx=0.5, rely=0.3, anchor="center") #Displays the question in the label
            self.question_no += 1


    def current_check_answer(self):
        if self.choosed_answer.get() == -1:  # Check if no answer is selected
            messagebox.showinfo("No Selection", "Please select an answer before proceeding.")
            return

        self.check_answer() #Calls the check_answer method to check if the answer is correct

    
    def check_answer(self):
        answer_mapping = {"a": 0, "b": 1, "c": 2, "d": 3}  # Map string answers to indices
        
        try:
            selected_answer = self.choosed_answer.get()  # Get the selected answer as an integer
            correct_answer = answer_mapping[self.questions[self.question_no - 1]["answer"]]  # Map correct answer to index

            self.root.after(1000, self.advance_question)  # Delay before moving to the next question

            if selected_answer == correct_answer:
                self.radio_btn[selected_answer].config(bg="green") # Highlight correct answer
                self.correct_ans += 1  
            else:
                self.radio_btn[selected_answer].config(bg="red")  # Highlight incorrect answer
                self.radio_btn[correct_answer].config(bg="green") # Highlight the correct answer
                self.wrong_ans += 1 
        except (KeyError, IndexError):
            messagebox.showinfo("Error", "An error occurred while checking the answer.")


    def advance_question(self):
        if self.question_no < len(self.questions):  
            self.display_question.config(text=self.questions[self.question_no]["question"].strip()) #Displays the question
            self.options_question_no()
            self.question_no += 1
        else:
            self.display_question.config(text="Quiz Completed!")
            self.display_question.place(relx=0.5, rely=0.4, anchor="center")
            self.next_button.config(text="Finish", command=self.root.quit)
            self.next_button.place(relx=0.5, rely=0.6, anchor="center")
            
            for btn in self.radio_btn:
                btn.place_forget()
            
            self.quiz_result() #Calls the quiz_result method to display the result

        
    def quiz_result(self):
        score = f"Score: {self.correct_ans}/{len(self.questions)}" #Calculates the number of correct answers
        messagebox.showinfo(f"Quiz Result", f"{score}") #Displays the result in a message box


    def options_question_no(self):
        radio_button = 0
        self.choosed_answer.set(-1)  # Reset the selected answer

        for choices in self.questions[self.question_no]["choices"]:
            self.radio_btn[radio_button]['text'] = choices.split(": ")[1].strip()
            self.radio_btn[radio_button].config(bg="SystemButtonFace")   # Set the text of the radio button
            radio_button += 1
        

    def choices_radio_btn(self):
        radio_buttons = []
        rely = 0.4

        while len(radio_buttons) < 4: 
            radio_btn = tk.Radiobutton(self.root, text="", 
                                       variable=self.choosed_answer, 
                                       value=len(radio_buttons), anchor="w")
            radio_btn.place(relx=0.4, rely=rely)
            radio_btn.config(font=("Arial", 12), wraplength=600)
            radio_buttons.append(radio_btn)
            rely += 0.05
            
        return radio_buttons


    
quiz = QuizReader("Existingfile.txt")
quiz.root.title("Quiz")
quiz.root.geometry("800x450")
quiz.root.mainloop()

