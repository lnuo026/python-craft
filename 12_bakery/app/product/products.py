# 基类 Product,__init__(self, name, price, recipe)。
     # price 用整数的"分"表示,比如 500 代表 5 元。
     # recipe 是字典,键是原料名,值是用量,比如 {"flour": 300, "sugar": 20, "butter": 30}。

# 在创建产品的那一刻,先检查传进来的价格合不合理,不合理就直接拒绝创建
# 在 __init__ 里加校验:price 不是整数或不大于 0,就抛 ValueError。
     # 这是上一课学的 raise 校验。

# 方法 unit_price(self),返回 self.price。
# 方法 describe(self),返回一句描述,比如名字加价格。
# Bread 继承 Product,不需要额外内容。
# Cake 继承 Product,多一个层数 layers。
     # __init__ 里用 super().__init__(...) 复用父类逻辑,再保存 layers。
     # 重写 unit_price,让价格随层数增加,比如基础价格加上每层若干分。


# 类里只需要把传进来的值存起来:真正的配方在创建对象的地方给(main)
class Product:
     def __init__(self, name, price, recipe: dict[str, int]):
          if not isinstance(price, int) or price <= 0:
               raise ValueError("price must be a positive integer")
          self.name = name
          self.price = price
          self.recipe = recipe

     def unit_price(self):
          return self.price

     # 通过 self.unit_price() 去取,Python 才会根据对象实际是面包还是蛋糕,调用各自版本的计价方法
     # 多态
     def describe(self):
          return f"{self.name} costs {self.unit_price()}"




     



