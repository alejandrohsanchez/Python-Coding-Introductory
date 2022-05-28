# Entering number of academic categories
correct_weight_verified = False
while(correct_weight_verified != True):
    number_of_classes = int(input("Enter the number of categories in your class: "))
    print()
    category_names = []
    category_weights = []
    for i in range(number_of_classes):
        category_names.append(input(f"""Enter the name of category {i+1} of {number_of_classes}: """))
        category_weights.append(float(input(f"""Enter the weight % for the "{category_names[i]}" category: """)))
        print()

    gradebook_verified = False
    while (gradebook_verified != True):
        print("Is this gradebook correct, yes or no?\n")
        for i in range(number_of_classes):
            print(f"""{category_names[i]}: {category_weights[i]}%""")
        print()
        correct = input("(yes or no): ")
        print()
        if (correct == 'yes'):
            gradebook_verified = True
            correct_weight_verified = True
        elif (correct == 'no'):
            gradebook_verified = True
            print("\nRestarting...\n")
        else:
            print("Incorrect input...\n")

# Grade entering and calculation
grade_entered = False
while (grade_entered != True):
    category_grades = []
    for i in range(number_of_classes):
        category_grades.append(float(input(f"""Enter your grade % for {category_names[i]}: """)))
        

    numerator = 0
    sum_of_weights = 0
    final_grade = 0

    for i in range(number_of_classes):
        numerator = numerator + (category_grades[i] * category_weights[i])
        sum_of_weights = sum_of_weights + category_weights[i];

    final_grade = numerator/sum_of_weights
    print(f"""\nYour final grade is: {round(final_grade, 2)}%\n""")

    submit_verified = False
    while (submit_verified != True):
        submit_answer = input("""Would you like to submit this grade to the gradebook or make grade changes?\n('submit' or 'make changes'): """)
        if (submit_answer == 'submit'):
            submit_verified = True
            grade_entered = True
            print("\nFinal grade submitted\n")

        elif (submit_answer == 'make changes'):
            submit_verified = True
            print("\nMaking changes...\n")
        
        else:
            print("Incorrect input...\n")