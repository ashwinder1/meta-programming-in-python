class House:
    num_rooms = 5
    bathrooms = 2

    def cost_evalutation(self, rate):
        cost = rate * self.num_rooms
        return cost
    
house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)