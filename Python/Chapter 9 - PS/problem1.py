with open("poems.txt") as f:
    data = f.read()

if "twinkle" in data:
    print("The poem contains the word twinkle")
else:
    print("The poem doesn't contain the word twinkle")