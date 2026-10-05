p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter a statement: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("It's a spam.")
else:
    print("It is not a spam.")