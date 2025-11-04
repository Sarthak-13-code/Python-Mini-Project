# GradeBook Analyzer
#Name: Sarthak Gupta
# Date: 4 November 2025

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    values = sorted(marks.values())
    n = len(values)
    if n % 2 == 0:
        return (values[n//2 - 1] + values[n//2]) / 2
    else:
        return values[n//2]

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

# Task 4: Grade Assignment
def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

# Task 5: Pass/Fail Lists 
def pass_fail_students(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed

# Task 6: Display Results 
def display_results(marks, grades):
    print("\n")
    print("Name\t\tMarks\tGrade")
    print()
    for name in marks:
        print(f"{name:<12}\t{marks[name]:<5}\t{grades[name]}")
    print("---------------------------------")

# Task 1 & 2 & 6: Main Menu
def main():
    print("")
    print("Welcome to GradeBook Analyzer")

    while True:
        print("\nMenu:")
        print("1. Enter student data manually")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            marks = {}
            n = int(input("Enter number of students: "))
            for i in range(n):
                name = input(f"Enter name of student {i+1}: ")
                score = int(input(f"Enter marks of {name}: "))
                marks[name] = score

            # Task 3: Statistical Analysis
            avg = calculate_average(marks)
            med = calculate_median(marks)
            max_score = find_max_score(marks)
            min_score = find_min_score(marks)

            print("\n===== STATISTICAL ANALYSIS =====")
            print(f"Average Marks: {avg:.2f}")
            print(f"Median Marks:  {med}")
            print(f"Highest Marks: {max_score}")
            print(f"Lowest Marks:  {min_score}")

            # Task 4: Grade Assignment
            grades = assign_grades(marks)

            # Grade distribution
            distribution = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
            for g in grades.values():
                distribution[g] += 1

            print("\n===== GRADE DISTRIBUTION =====")
            for grade, count in distribution.items():
                print(f"{grade}: {count} students")

            # Task 5: Pass/Fail
            passed, failed = pass_fail_students(marks)
            print("\n===== PASS/FAIL SUMMARY =====")
            print(f"Passed ({len(passed)}): {', '.join(passed)}")
            print(f"Failed ({len(failed)}): {', '.join(failed)}")

            # Task 6: Display Results
            display_results(marks, grades)

            print("\nAnalysis Complete!")

        elif choice == '2':
            print("Exiting GradeBook Analyzer. Thank you!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()