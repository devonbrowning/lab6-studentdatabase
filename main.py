# Name List
names = ['Sammy', 'Sally', 'Susan']
# Hometown List
hometowns = ['Denver', 'Los Angeles', 'Dallas']
# Favorite Foods List
favorite_food = ['Sushi', 'Burger', 'Pasta']

#validate user input for student number
def desired_student_number(num):
    if num < 1 or num > len(names):
        print("Invalid number. Please enter a number between 1 and {}.".format(len(names)))
        return False
    return True

#Validate user input for category
def desired_category(category):
    if category.lower() not in ["hometown", "favorite food"]:
        print("Invalid category. Please enter 'hometown' or 'favorite food'.")
        return False
    return True

#Show student info
def student_info(student_number, category):
    index = student_number - 1
    print("Student Name: ", names[index])
    if category.lower() == "hometown":
        print("Hometown: ", hometowns[index])
    else:
        print("Favorite Food: ", favorite_food[index])

# Loop
while True:
    # Prompt user for student number
    student_number = int(input("Please enter the student number (1 to {}): ".format(len(names))))
    if not desired_student_number(student_number):
        continue

# Prompt user for category
    category = input("What category do you want to display? (Hometown/Favorite Food): ")
    if not desired_category(category):
        continue

# Show student info
    student_info(student_number, category)

#Ask user if they want to learn about naother student
    another = input("Do you want to learn about another student? (yes/no): ")
    if another.lower() != "yes":
        break