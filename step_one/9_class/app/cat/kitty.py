from app.Pet.pet import pet
class cat(pet):
     def __init__(self, name, age, mood, temperature):
          super().__init__(name, temperature)
          self.age = age
          self.mood = mood
     
     def action(self):
          print(f"the cat is {self.name}, jumping into a leak")

     def is_emergency(self):
          return self.temperature >= 39.5