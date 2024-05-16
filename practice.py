### with help to see how to do extended challenge
# Student information
students = [
    {"name": "Sammy", "hometown": "Denver", "favorite_food": "Sushi"},
    {"name": "Sally", "hometown": "Los Angeles", "favorite_food": "Burger"},
    {"name": "Susan", "hometown": "Dallas", "favorite_food": "Pasta"}
]

# Function to validate user input for student number
def validate_student_number(num):
    if num < 1 or num > len(students):
        print("Invalid number. Please enter a number between 1 and {}.".format(len(students)))
        return False
    return True

# Function to validate user input for category
def validate_category(category):
    if category.lower() not in ["hometown", "favorite_food"]:
        print("Invalid category. Please enter 'hometown' or 'favorite_food'.")
        return False
    return True

# Function to show student info
def show_student_info(student, category):
    print("Student Name:", student["name"])
    if category.lower() == "hometown":
        print("Hometown:", student["hometown"])
    else:
        print("Favorite Food:", student["favorite_food"])

# Function to show list of all students
def show_all_students():
    print("List of all students:")
    for index, student in enumerate(students, start=1):
        print("{}. {}".format(index, student["name"]))

# Function to search for a student by name
def search_student_by_name(name):
    name = name.lower()
    found = False
    for student in students:
        if name in student["name"].lower():
            print("Student found:")
            show_student_info(student, "all")
            found = True
    if not found:
        print("No student found with that name.")

# Main loop
while True:
    print("\nMenu:")
    print("1. See list of all students")
    print("2. Search student by name")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_students()
    elif choice == "2":
        search_name = input("Enter student name to search: ")
        search_student_by_name(search_name)
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
