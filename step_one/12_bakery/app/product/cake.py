from app.product.products import Product

class Cake(Product):
     def __init__(self, name, price, recipe, layer):
          super().__init__(name, price, recipe)
          self.layer = layer

     def unit_price(self):
          return super().unit_price() + self.layer * 20