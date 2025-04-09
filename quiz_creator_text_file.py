import os 

def file_maker(): 
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
            file_name = input("Enter a new file name: ")
            return file_name 
    else: 
        return file_name

#Function to asks the user for questions and answers and writes them to the file
def create_quiz():
    #Get the file name from the user
    file_name = file_maker()

    #Open the file in write mode to create a new quiz file
    with open(file_name, "a") as quiz_file:
        quiz_file.write("Quiz Creator\n")
        quiz_file.write("\n")

        #While true for a loop to allow the user to decide when to stop entering questions
        while True: 
            question = input("Enter a question: ") 
            quiz_file.write(f"Question: {question}\n") 
            
            #Ask the user for choices 
            for i in range(4): 
                if i == 0: 
                    choice = input("Enter choice a: ")
                    quiz_file.write(f"Choice a: {choice}\n")
                if i == 1: 
                    choice = input("Enter choice b: ")
                    quiz_file.write(f"Choice b: {choice}\n")
                if i == 2:
                    choice = input("Enter choice c: ")
                    quiz_file.write(f"Choice c: {choice}\n")
                if i == 3:
                    choice = input("Enter choice d: ")
                    quiz_file.write(f"Choice d: {choice}\n")
            
            #Ask the user for the correct answer
            answer = input("Enter the correct answer (a, b, c, d): ")
            quiz_file.write(f"Answer: {answer}\n")
            quiz_file.write("\n")
            
            #Ask the user if they want to add another question
            another = input("Do you want to add another question? (yes/no): ")
            if another.lower().strip() != "yes":
                break

create_quiz()

