with open("file.txt") as f:
    content1 = f.read()

with open("file_copy.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes the files are identical.")
else:
    print("The files are not identical.")