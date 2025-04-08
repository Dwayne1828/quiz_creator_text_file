
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
            break

create_quiz()

