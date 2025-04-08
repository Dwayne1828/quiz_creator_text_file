
#Function to asks the user for questions and answers and writes them to the file
def create_quiz():
    #Open the file in write mode to create a new quiz file
    with open("quiz.txt", "w") as quiz_file:
        quiz_file.write("Quiz Creator\n")
        quiz_file.write("\n")

        #While true for a loop to allow the user to decide when to stop entering questions
        while True: 
            question = input("Enter a question: ") 
            quiz_file.write(f"Question: {question}\n") 
            break

create_quiz()

