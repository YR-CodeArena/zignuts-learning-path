class Train:
    def book_ticket(self):
        self.name = input("Enter your name: ")
        self.source = input("Enter your source: ")
        self.destination = input("Enter your destination: ")
        print(f"You are {self.name}. Your source is {self.source} and destination is {self.destination}.")

    def getStatus(self):
        self.status = input("Enter the no of seats: ")
        print(f"No of seats: {self.status}")

    def fare(self):
        self.price = 2000
        print(self.price)

obj0 = Train()
obj0.book_ticket()
obj0.getStatus()
obj0.fare()