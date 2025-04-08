
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
                choice = input("Enter choices (A, B, C, D): ")
                if i == 0: 
                    quiz_file.write(f"Choice A: {choice}\n")
                if i == 1: 
                    quiz_file.write(f"Choice B: {choice}\n")
                if i == 2:
                    quiz_file.write(f"Choice C: {choice}\n")
                if i == 3:
                    quiz_file.write(f"Choice D: {choice}\n")
            
            break
        
create_quiz()

