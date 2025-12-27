from random import randint
# Craeting class in Python.
class Train:
    def __init__(self, trainNo,PassengerName):
        self.trainNo = trainNo
        self.PassengerName = PassengerName

    def bookTicket(self, fro, to):
        print(f"The ticket is booked in train no. {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train number: {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

# Creating object
t = Train(1233,"Ritesh Kumar")
t.name = "Ritesh Kumar"
print(f"Passenger name is {t.name}.")
t.bookTicket("Karnal", "Delhi")
t.getStatus()
t.getFare("Karnal", "Delhi")
