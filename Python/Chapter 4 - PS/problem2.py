a = int(input("Enter the first student marks: "))
b = int(input("Enter the second student marks: "))
c = int(input("Enter the third student marks: "))
d = int(input("Enter the fourth student marks: "))
e = int(input("Enter the fifth student marks: "))
f = int(input("Enter the sixth student marks: "))

l = [a, b, c, d, e, f]
print(l)
l.sort()
print("Sorted marks: ", l)