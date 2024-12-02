class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}  # Dictionary to store subjects, marks, and grades

    def add_grade(self, subject, marks, grade):
        if subject not in self.subjects:
            self.subjects[subject] = []
        self.subjects[subject].append({"marks": marks, "grade": grade})

    def subject_average(self, subject):
        if subject in self.subjects and self.subjects[subject]:
            total_marks = sum(entry["marks"] for entry in self.subjects[subject])
            return total_marks / len(self.subjects[subject])
        return 0.0

    def overall_average(self):
        total_marks = []
        for entries in self.subjects.values():
            total_marks.extend(entry["marks"] for entry in entries)
        if total_marks:
            return sum(total_marks) / len(total_marks)
        return 0.0

    def __str__(self):
        result = f"Student: {self.name}\n"
        for subject, entries in self.subjects.items():
            avg_marks = self.subject_average(subject)
            grades_and_marks = ", ".join(
                f"{entry['marks']} ({entry['grade']})" for entry in entries
            )
            result += f"  {subject}: [{grades_and_marks}], Average Marks: {avg_marks:.2f}\n"
        result += f"Overall Average Marks: {self.overall_average():.2f}\n"
        return result


class GradeTracker:
    def __init__(self):
        self.students = {}  # Dictionary to store student objects by name

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student '{name}' has been added.")
        else:
            print(f"Student '{name}' already exists.")

    def add_grade(self, name, subject, marks, grade):
        if name in self.students:
            self.students[name].add_grade(subject, marks, grade)
            print(f"Grade '{grade}' with marks {marks} added for '{name}' in {subject}.")
        else:
            print(f"Student '{name}' not found.")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

    def run(self):
        while True:
            print("\n--- Student Grade Tracker ---")
            print("1. Add Student")
            print("2. Add Grade")
            print("3. View All Students")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter the student's name: ")
                self.add_student(name)
            elif choice == "2":
                name = input("Enter the student's name: ")
                subject = input("Enter the subject: ")
                try:
                    marks = float(input("Enter marks: "))
                    grade = input("Enter grade (e.g., A, B, C): ").upper()
                    if grade not in ["A", "B", "C", "D", "F"]:
                        print("Invalid grade. Enter grades as A, B, C, D, or F.")
                        continue
                    self.add_grade(name, subject, marks, grade)
                except ValueError:
                    print("Invalid input for marks. Please enter a number.")
            elif choice == "3":
                self.view_all_students()
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = GradeTracker()
    tracker.run()
