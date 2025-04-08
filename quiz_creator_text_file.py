
#Open a text file to store the quiz questions and answers
with open("quiz.txt", "w") as quiz_file:
    quiz_file.write("Quiz Creator\n")

#Function to asks the user for questions and answers and writes them to the file
def create_quiz(quiz_file):
    #While true for a loop to allow the user to decide when to stop entering questions
    while True: 
        question = input("Enter a question: ") 
        quiz_file.write(f"Question: {question}\n") 

create_quiz(quiz_file) 
