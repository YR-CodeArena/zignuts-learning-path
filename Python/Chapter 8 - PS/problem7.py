l = ["Yash", "Soham", "Sohan", False, 56.76, 7, "Rohan"]
name = input("Type a name: ")
def rem():
    l.remove(name)
    print(l)
    a = name.strip("an")
    print(a)

rem()
