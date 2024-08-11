class Employees:
    def __init__(self, name, last) -> None:
        self.name = name 
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take leave for " + str(days) + " days"
    
adrian = Supervisors("Adrian", "A", "apple") #supervisor

emily = Chefs("Emily", "E") # chef 1
juno = Chefs("Juno", "J") # chef 2

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)
