from app.Pet.pet import pet
class dog(pet):
     def __init__(self, name, age, temperature):
          super().__init__(name, temperature)
          self.age = age

     def is_emergency(self):
          return self.temperature >= 39