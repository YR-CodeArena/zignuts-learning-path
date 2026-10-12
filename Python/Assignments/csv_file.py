import csv

filename = "students.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)