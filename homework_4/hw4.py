import csv
import json
from pathlib import Path


def save_shopping_list(items):
    with open("shopping.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(f"{item}\n")



items1 = [
"Milk",
"Bread",
"Apples",
"Coffee"
]



save_shopping_list(items1)



with open("students.csv", "w", encoding="utf-8", newline="") as students_names:
    writer = csv.writer(students_names)

    writer.writerow(["name", "age"])
    writer.writerow(["Anna", "21"])
    writer.writerow(["Tom", "19"])
    writer.writerow(["Kate", "22"])



def read_students(filename):
    with open(filename, "r", encoding="utf-8", newline="") as students:
        reader = csv.DictReader(students)
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")


read_students("students.csv")




def save_profile(name,age,city):
    profile_data = {"name": name, "age": age, "city": city}
    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile_data, file, indent=2, ensure_ascii=False)


save_profile("Maria", 30, "Haifa")


def create_reports_folder():
    reports_dir = Path("reports_1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir/"result.txt"
    with open (result_file, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!")



create_reports_folder()