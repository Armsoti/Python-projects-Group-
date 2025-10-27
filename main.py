from random import choice

def new_student():
    Name = input("Enter your name: ")
    Year = int(input("Enter Year of studying(from 1 to 4): "))
    while Year < 1 or Year > 4:
        Year = int(input("Enter Year of studying(from 1 to 4): "))
    Group = input("Enter Group: ")
    Subject_and_graduates = {}
    while True:
        Subject = input("Enter Subject (or press Enter to finish): ")
        if not Subject:
            break
        Mark = int(input("Enter Mark of Subject: "))
        Subject_and_graduates[Subject] = Mark

    student_data = {
        "Year": str(Year),
        "Group": Group,
        "Subjects and graduates": Subject_and_graduates
    }

    return Name, student_data

#Голишев Артем - функція видалення даних
def delete_student(students):
    m = input("Enter full name of student to delete: ")
    if m in students:
        confirm = input(f"Are you sure you want to delete '{m}'? 1-yes 2-no: ")
        if confirm == '1':
            del students[m]
            print(f"Student '{m}' has been successfully deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No student found with name '{m}'.")

students = {
    "Мартиненко Костянтин Вікторович": {
        "Year": "2",
        "Group": "КН-41",
        "Subjects and graduates": {
            "Алгоритми і структури даних": 70,
            "Програмування мовою Python": 88,
            "Чисельні методи": 90,
        }
    },

    "Коваленко Ірина Сергіївна": {
            "Year": "1",
            "Group": "КН-43",
            "Subjects and graduates": {
                "Вища математика": 65,
                "Основи програмування": 90,
                "Англійська мова": 94,
            }
        },

    "Оніщенко Максим Ігоревич": {
            "Year": "1",
            "Group": "КН-41",
            "Subjects and graduates": {
                "Вища математика": 70,
                "Основи програмування": 69,
                "Англійська мова": 99,
            }
        }
}

choice_to_add_student = int(input("Do you want to add new student? 1-yes 2-no"))

if choice_to_add_student == 1:
    n = int(input("How many students do you want to add?"))
    while n < 1:
        n = int(input("How many students do you want to add?"))
    for i in range(n):
        student_name, new_data = new_student()
        students[student_name] = new_data
        print(f"Student '{student_name}' added successfully.")

choice_to_delete_student = int(input("Do you want to delete a student? 1-yes 2-no"))

if choice_to_delete_student == 1:
    delete_student(students)

for key, value in students.items():
    print(key, value)
print("-"*15)
