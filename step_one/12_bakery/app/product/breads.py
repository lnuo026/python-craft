from app.product.products import Product

class Breads(Product):
     def __init__(self, name, price, recipe, kind):
          super().__init__(name, price, recipe)
          self.kind = kind
