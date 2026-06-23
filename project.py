import csv
import matplotlib.pyplot as plt
def main():
    
    students = load_students(r"C:\Python For DS\students.csv")
    plot_top_3_students(students)
    print("\n STUDENT DATA ANALYZER \n")

    for student in students:
        grade = get_grade(student["average"])
        print(
            f"Name: {student['name']} | "
            f"Marks: {student['total_marks']} | "
            f"Avg: {student['average']} | "
            f"Grade: {grade}"
        )

    print("\n----------------------------------")
    print("Total Students:", count_students(students))
    print("Class Average:", calculate_average(students))
    print("Highest Scorer:", find_top_student(students))
    print("Lowest Scorer:", find_lowest_student(students))

def load_students(filename):
    students = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["total_marks"] = int(row["total_marks"])
            row["average"] = float(row["average"])
            students.append(row)

    return students


def count_students(students):
    return len(students)

def calculate_average(students):
    total = 0
    for student in students:
        total += student["average"]
    return round(total / len(students), 2)

def find_top_student(students):
    top = students[0]
    for student in students:
        if student["total_marks"] > top["total_marks"]:
            top = student
    return top["name"]

def find_lowest_student(students):
    lowest = students[0]
    for student in students:
        if student["total_marks"] < lowest["total_marks"]:
            lowest = student
    return lowest["name"]

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def plot_top_3_students(students):
    sorted_students = sorted(
        students,
        key=lambda x: x["total_marks"],
        reverse=True
    )

    top3 = sorted_students[:3]

    names = [s["name"] for s in top3]
    marks = [s["total_marks"] for s in top3]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(names, marks, color="green")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(height),
            ha="center",
            va="bottom"
        )

    plt.title("Top 3 Students")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")

    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()