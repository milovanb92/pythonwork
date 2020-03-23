from random import choice

class Lottery:
    """Class that uses list of numbers and comare it with custom numbers of ticket"""

    def __init__(self, nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 's', 'r', 'g']):
        """Define list of numbers for lottery"""
        self.number = nums
        self.ticket_played = 0
    
    def ticket(self):
        """Make a random ticket contained 4 characters from previous defined numbers"""
        win_tikcet = []
        win_tikcet.append(choice(self.number))
        win_tikcet.append(choice(self.number))
        win_tikcet.append(choice(self.number))
        win_tikcet.append(choice(self.number))
        return win_tikcet     

    def increment_ticket_played(self):
        self.ticket_played += 1


my_ticket = [1, 4, 's', 'r']

ticket = Lottery()
ticket.ticket()

if my_ticket != ticket.ticket():
    while ticket.ticket() != my_ticket:
        ticket.ticket()
        ticket.increment_ticket_played()
        print(f"pokusaj broj {ticket.ticket_played}")
    print(f"Vas tiket je dobitni iz {ticket.ticket_played}-og pokusaja.")

