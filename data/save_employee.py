import csv
import os


def save_employee(employee):
    file_path = "data/employees.csv"

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=employee.keys())

        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writeheader()

        writer.writerow(employee)