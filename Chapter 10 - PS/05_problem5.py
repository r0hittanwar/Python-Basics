# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint

class Train:
    @staticmethod
    def greet():
        print("Welcome to Indian Railway")

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"Ticket has booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getInfo(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(200, 6000)}")


rail = Train(5048)
rail.greet()
rail.bookTicket("Agra", "Mathura")
rail.getStatus()
rail.getInfo("Agra", "Mathura")