class pet:
     def __init__(self, name, temperature):
          self.name = name
          self.temperature = temperature

     def is_emergency(self):
          return self.temperature > 38

     
          