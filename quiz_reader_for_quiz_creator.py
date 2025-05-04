
def quiz_reader(): 
    with open("Existingfile.txt", "r") as file:
        lines = file.readlines() #Stores the lines in a list 
 
        #Create a dictionary to store the questions, choices, and answers
        questions = {"choices": []} #Initialize the dictionary with empty lists for choices and answer

        #Iterate through the lines to check for the presence of a question, choices, and answer
        for line in lines: 
            line = line.strip() #Removes leading and trailing whitespace
            
            if "Quiz Created" in line: #Checks if the line contains the word "Quiz Created"
                continue #If it does, skip the line
            if "Choice" in line: #Checks if the line contains the word "Choice"
                questions["choices"].append(line) #Adds the choices into the choices list

        print(questions)

quiz_reader()


