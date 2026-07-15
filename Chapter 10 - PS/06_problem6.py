'''Can you change the self-parameter inside a class to something else (say “harry”).
Try changing self to “slf” or “harry” and see the effects.'''

from random import randint

class Train:
    @staticmethod
    def greet():
        print("Welcome to Indian Railway")

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def bookTicket(harry, fro, to):
        print(f"Ticket has booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getInfo(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(200, 6000)}")


rail = Train(5048)
rail.greet()
rail.bookTicket("Agra", "Mathura")
rail.getStatus()
rail.getInfo("Agra", "Mathura")