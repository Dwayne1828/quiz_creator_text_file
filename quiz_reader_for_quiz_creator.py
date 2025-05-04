
def quiz_reader(): 
    with open("Existingfile.txt", "r") as file:
        lines = file.readlines()
        print(lines)

quiz_reader()

