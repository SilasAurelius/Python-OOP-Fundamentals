"""
Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
"""
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0 
        
    def add_participant(self):
        self.participant_count += 1 
    
    def get_participant_count(self):
        return self.participant_count 

event = Event("Coding Temple Code-athon", "08-05-2024")
event.add_participant()
count = event.get_participant_count()
print(f"Current participant count: {count}") 
