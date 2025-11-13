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

#Голишев Артем - продовження, друге питання та відповідь на попереднє
file_3 = Open(file1_name, "a")

if (file_3 != None):
    file_3.write("Artem Holyshev\n")
    file_3.write("""Answer:\nList and tuple are collections of data that are ordered.
However, the main difference is that the first one is changeable, while the second one is not.
Other differences include better memory efficiency and better iteration for tuples, as well as different syntax:
A list is written in square brackets [ ], and a tuple is written in parentheses ( ).\n""")
    file_3.write("Next question:\nWhat is a dictionary in Python and how does it work?\n")
    print("Information was successfully added to test.txt!")
    file_3.close()
    print("File test.txt was closed!")

#Козинець Володимир - продовження, відповідь на останнє питання
file_4 = Open(file1_name, "a")

if (file_4 != None):
    file_4.write("Volodymyr Kozynets\n")
    file_4.write("""Answer:\nDictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values.\n""")
    print("Information was successfully added to test.txt!")
    file_4.close()
    print("File test.txt was closed!")


file_1_r = Open(file1_name, "r") #Це в кінець коду для виводу змісту файлу
original_text = file_1_r.read()
print(original_text)
