data = {
    "company": "Zignuts",
    "location": "Ahmedabad",
    "employees": [
        {
            "id": 101,
            "name": "Amit",
            "skills": ["Python", "Django"]
        },
        {
            "id": 102,
            "name": "Pooja",
            "skills": ["HTML", "CSS", "JavaScript"]
        }
    ]
}

company_name = data["company"]
city = data["location"]
emp_list = data["employees"]

print("Company:", company_name)
print("Location:", city)

for emp in emp_list:
    emp_id = emp["id"]
    emp_name = emp["name"]
    skill_list = emp["skills"]
    print("---")
    print("ID:", emp_id)
    print("Name:", emp_name)
    print("Skills:")
    for skill in skill_list:
        print("-", skill)