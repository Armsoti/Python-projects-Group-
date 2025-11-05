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




file_1_r = Open(file1_name, "r") #Це в кінець коду для виводу змісту файлу
original_text = file_1_r.read()
print(original_text)