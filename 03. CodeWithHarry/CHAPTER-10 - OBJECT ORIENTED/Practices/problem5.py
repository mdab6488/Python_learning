from random import randint

print()

class Train:

    def __init__(self, train_number):
        self.train_number = train_number

    def book(self,
             start,
             end):
        print(f"Ticket is booked in train no: {self.train_number} from '{start}' to '{end}'")

    def get_status(self):
        print(f"Train no: {self.train_number} is running on time")

    def get_fare(self,
                 start,
                 end):
        print(f"Ticket fare in train no: {self.train_number} from '{start}' to '{end}' is {randint(222, 555)}")


t = Train(12399)
t.book(start="Dhaka", end="Muksudpur")
print()
t.get_status()
print()
t.get_fare(start="Dhaka", end="Muksudpur")