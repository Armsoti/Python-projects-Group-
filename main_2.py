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

#Ющенко Альона - функція сортування даних
def sort_students(students):
    print("Sort by:")
    print("1 - Name")
    print("2 - Year of studying")
    print("3 - Average mark")
    print("4 - Group")
    s = input("Enter your choice: ")

    if s == '1':
        sorted_students = dict(sorted(students.items(), key=lambda x: x[0]))

    elif s == '2':
        sorted_students = dict(sorted(students.items(), key=lambda x: int(x[1]["Year"])))

    elif s == '3':
        def average_mark(student):
            marks = student["Subjects and graduates"].values()
            return sum(marks) / len(marks) if marks else 0

        sorted_students = dict(sorted(
            students.items(),
            key=lambda x: average_mark(x[1]),
            reverse=True
        ))

    elif s == '4':
        sorted_students = dict(sorted(students.items(), key=lambda x: x[1]["Group"]))

    else:
        print("Invalid choice. Showing unsorted list.")
        return students

    return sorted_students

#Козинець Володимир - функція пошуку даних
def search_students(students):
    print("Search by:")
    print("1 - Name")
    print("2 - Year of studying")
    print("3 - Subjects")
    print("4 - Group")
    s = input("Enter your choice: ")

    search_results = {}

    if s == '1':
        query = input("Enter name (or part of name) to search: ")
        for name, data in students.items():
            if query.lower() in name.lower():
                search_results[name] = data
    elif s == '2':
        query = input("Enter year of studying (1-4): ")
        for name, data in students.items():
            if data["Year"] == query:
                search_results[name] = data
    elif s == '3':
        query = input("Enter subject name (or part of name): ")
        for name, data in students.items():
            for subject in data["Subjects and graduates"].keys():
                if query.lower() in subject.lower():
                    search_results[name] = data
                    break
    elif s == '4':
        query = input("Enter group name (or part of name): ")
        for name, data in students.items():
            if query.lower() in data["Group"].lower():
                search_results[name] = data
    else:
        print("Invalid choice. Returning no results.")

    if search_results:
        print("Search results: ")
        for key, value in search_results.items():
            print(key, value)
        print('-' * 15)
    else:
        print("No results!")

    return search_results

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

choice_to_add_student = int(input("Do you want to add new student? 1-yes 2-no "))

if choice_to_add_student == 1:
    n = int(input("How many students do you want to add? "))
    while n < 1:
        n = int(input("How many students do you want to add? "))
    for i in range(n):
        student_name, new_data = new_student()
        students[student_name] = new_data
        print(f"Student '{student_name}' added successfully.")

choice_to_delete_student = int(input("Do you want to delete a student? 1-yes 2-no "))

if choice_to_delete_student == 1:
    delete_student(students)

choice_to_sort = int(input("Do you want to sort students? 1-yes 2-no "))
if choice_to_sort == 1:
    students = sort_students(students)

choice_to_search = int(input("Do you want to search students? 1-yes 2-no "))
if choice_to_search == 1:
    search_students(students)

for key, value in students.items():
    print(key, value)
print("-"*15)