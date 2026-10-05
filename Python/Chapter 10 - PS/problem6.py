class Train:
    def book_ticket(yash):
        yash.name = input("Enter your name: ")
        yash.source = input("Enter your source: ")
        yash.destination = input("Enter your destination: ")
        print(f"You are {yash.name}. Your source is {yash.source} and destination is {yash.destination}.")

    def getStatus(yash):
        yash.status = input("Enter the no of seats: ")
        print(f"No of seats: {yash.status}")

    def fare(yash):
        yash.price = 2000
        print(yash.price)

obj0 = Train()
obj0.book_ticket()
obj0.getStatus()
obj0.fare()