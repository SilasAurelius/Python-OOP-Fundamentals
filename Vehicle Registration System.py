"""Task 1: Vehicle Registration System
Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
"""

class Vehicle:
    def __init__(self, reg_num, type, owner):
            self.reg_num = reg_num
            self.type = type
            self.owner = owner
            
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"New owner is: {self.owner}")
            
            
vehicle1 = Vehicle("123abc", "motorcycle", "Silas") 
vehicle2 = Vehicle("456def", "car", "Cherie")
vehicle3 = Vehicle("789ghi", "train", "Bob")

print(f"Vehicle 1's owner: {vehicle1.owner}.")
print(f"Vehicle 2's owner: {vehicle2.owner}.")
print(f"Vehicle 3's owner: {vehicle3.owner}.")

vehicle1.update_owner("Sarah")
vehicle2.update_owner("Cindy")
vehicle3.update_owner("Sigmund")

print(f"Vehicle 1 is a {vehicle1.type} with the registration number: {vehicle1.reg_num} - Owner: {vehicle1.owner}.")
print(f"Vehicle 2 is a {vehicle2.type} with the registration number: {vehicle2.reg_num} - Owner: {vehicle2.owner}.")
print(f"Vehicle 3 is a {vehicle3.type} with the registration number: {vehicle3.reg_num} - Owner: {vehicle3.owner}.")
                
"""Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners."""