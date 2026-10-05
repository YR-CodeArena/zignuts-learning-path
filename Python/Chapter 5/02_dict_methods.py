marks = {
    "Yash" : 100,
    "Aakash" : 67,
    "Jiya" : 78
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Yash" : 99, "Ira" : 89})
# print(marks)
print(marks.get("Yash2"))  #prints None
# print(marks["Yash2"]) # Returns an error

# value = marks.pop("Jiya")
# print(value)

item = marks.popitem()
print(item)