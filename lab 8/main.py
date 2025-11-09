#Дарія Щербань - створення файлу та перше питання

def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "test.txt"
file_1_w = Open(file1_name, "w")

if(file_1_w != None):
    file_1_w.write("Dariia Shcherban\n")
    file_1_w.write("What is the complete form of a conditional operator if?\n")
    print("Information was successfully added to test.txt!")
    file_1_w.close()
    print("File test.txt was closed!")

#Ющенко Альона - надання відповіді на питання, та додавання наступного
file_2 = Open(file1_name, "a")  # "a" означає "append" — дописати в кінець файлу

if (file_2 != None):
    file_2.write("Yushchenko Alona\n")
    file_2.write("""Answer:\nIt checks whether a certain condition is true, and if it is, the statement inside the block will be executed.
In Python, indentation is used to define the block of code that belongs to the if statement.\n""")
    file_2.write("New questions:\nWhat is the difference between a list and a tuple in Python?\n")
    print("Information was successfully added to test.txt!")
    file_2.close()
    print("File test.txt was closed!")


file_1_r = Open(file1_name, "r") #Це в кінець коду для виводу змісту файлу
original_text = file_1_r.read()
print(original_text)