
def quiz_reader(): 
    with open("Existingfile.txt", "r") as file:
        lines = file.readlines() #Stores the lines in a list 
 
        complete_Questions = [] #Initialize an empty list to store the questions with answer and choices
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
                complete_Questions.append(questions) #Adds the question to the Questions list
                questions = {"question": "", "choices": [], "answer": None} #Resets the dictionary for the next question
        
        print(complete_Questions)

quiz_reader()


