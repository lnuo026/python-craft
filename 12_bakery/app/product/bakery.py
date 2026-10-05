# 仓库：2个功能：
# 存的东西,也就是它的属性:
# self.ingredients:原料仓库,存着面粉、糖、黄油、鸡蛋各有多少
# self.product_stock:成品仓库,存着烘焙好的各种面包蛋糕有多少
# self.catalog:产品目录,记着这家店会做哪些产品、各自的配方

# 能做的操作,也就是它的方法:
# register(product):往目录里登记一个新产品
# bake(name, quantity):检查原料够不够,够就扣原料、加成品
# 要记住原料库存和成品库存两份状态。
# 需要保存三样东西:

# 原料库存字典,比如 {"flour": 5000, "sugar": 1000, "butter": 800, "eggs": 30}
# 成品库存字典,开始是空的
# 产品目录:一个字典,键是产品名,值是产品对象。需要一个方法把产品登记进去,比如 register(product)。注意目录以名字为键,所以每个产品名要唯一,你现在测试数据里有两个都叫 "bread",以后用名字查就会冲突,换成不同的名字,比如 "white bread"、"rye bread"。

# 核心是 bake(name, quantity),按这个顺序做:
# 产品名不在目录里,抛 UnknownProduct。数量不是正整数,抛 ValueError。
# 对配方里的每种原料,算出需要的总量(单份用量乘以数量),和库存比较,把不够的原料连同缺口记录下来。这一步只检查,不要修改任何库存。
# 如果有任何缺口,抛 InsufficientIngredients,并在信息里说明缺哪种原料、缺多少。
# 全部够了,才统一扣减原料。
# 最后把成品库存里这个产品的数量加上去。


# 字典自带的方法
# .get(key, default) 按键取值,键不存在时不报错,返回你给的默认值:
# .items() 一次取出每一对"键和值",常和 for 一起用:
# for key, value in d.items():
#     print(key, value)        # flour 200, then sugar 150

# 每一轮循环拿到的是一个二元组,被拆开赋给 key 和 value。你的代码里 for ingredient, per_unit in product.recipe.items(): 就是这个用法。
# 字典还有两个同类的方法
# d.keys()      # all the keys:   dict_keys(['flour', 'sugar'])
# d.values()    # all the values: dict_values([200, 150])



from app.exceptions import UnknownProduct, InsufficientIngredients, OutOfstock
from app.product.breads import Breads
from app.product.cake import Cake

class Bakery:
     def __init__(self, ingredients):
          # 原料库存
          self.ingredients = ingredients
          # 可以直接在class里面赋一个固定的初始值

          # 成品库存
          self.product_stock ={}
          # 产品目录
          self.catalog = {}
          self.requests = {}


# 产品登记 + 产品目录
     def register(self, product, quantity=0):
          # self.catalog[...] = ...   是字典的赋值,键不存在就新增一对,键已存在就覆盖。
          # product 是整个对象,完整的信息，用 name 做标签,把整个对象存在这个标签下面
          self.catalog[product.name] = product
          # 两个字典用同一个 name 做键,各自存不同的东西:
          # catalog 里存"这个产品是什么"(对象),product_stock 里存"这个产品现在有几个"(数字)。
          self.product_stock[product.name] = self.product_stock.get(product.name, 0) + quantity
          
          # 增加新的陌生订单
          self.requests.pop(product.name, None)



     def bake(self, name, quantity):
          if name not in self.catalog:
               raise UnknownProduct(f"unknown product: {name}")
          elif not isinstance(quantity, int)or quantity <= 0:
               raise ValueError("must be a positive integer")

          #算需要量并记录缺口、有缺口就抛 InsufficientIngredients。
          # 没缺口再统一扣减、最后增加成品库存。
          missing = {}
          # = self.catalog[name] 右边查找 
          registered = self.catalog[name]

          # unit_ingredient 和 per_unit 不是"从对象里挑出来的两个属性"
          # 它们是遍历 recipe 这个字典时,每一轮自动得到的"键"和"值"。它们不需要提前定义
          for ingredient_name, per_unit in registered.recipe.items():
               needed = per_unit * quantity
               # self.ingredients 是总库存字典,就是 Bakery 创建时传进去的
               # 用这个键去总库存里找对应的数量,找不到就当 0,available = 库存里这种原料现在有多少
               available = self.ingredients.get(ingredient_name, 0)
               if available < needed:
                    # 字典赋值:左边指定"哪一项",右边是"存什么值"
                    missing[ingredient_name] = needed - available
                    # missing 是空字典,说明每一种原料都够,可以动手扣减。
                    # missing 里有东西,说明至少一种不够,直接抛 InsufficientIngredients,里面列出所有不够的原料,不是只报第一个。

          if missing:
               raise InsufficientIngredients(f"missing ingredients: {missing}")

          for ingredient_name, per_unit in registered.recipe.items():
               self.ingredients[ingredient_name] -= per_unit * quantity
          self.product_stock[name] = self.product_stock.get(name, 0) + quantity




     # 顾客可以一次买多种。订单是一个字典,每一项的键是产品名,值是"这一种买几个"。
     # 数量不是整张订单共用一个,而是跟着各自的产品名走
     def order(self, lists_from_customer):
     
     # 先找出所有未知产品,记下来再拒绝;数量检查放在后面
          unknown =[]
          for name in lists_from_customer:
               if name not in self.catalog:
                    unknown.append(name)

          if unknown:
               for i in unknown:
                    self.requests[i] = self.requests.get(i, 0) + 1
               raise UnknownProduct(f"unknow product: {i}, we will prepare this next time")


          for name, quantity in lists_from_customer.items():
               if not isinstance(quantity, int) or quantity <= 0:
                    raise ValueError(f"invalid quantity for {name} : {quantity}")

          short = {}
          for name, quantity in lists_from_customer.items():
               available = self.product_stock.get(name, 0)
               if available < quantity:
                    # name 对应的东西赋值上数字
                    short[name] = quantity - available

          
          # step 3: any shortage -> refuse the whole order
          if short:
               raise OutOfstock(f"not enough stock, missing: {short}")


          # step 4: deduct stock, price each line, build the receipt
          total = 0
          lines = []
          for name, quantity in lists_from_customer.items():
               # 右边用 name 当键,从库存里读出当前数量;
               # 减去要买的数量;结果再存回同一个键。
               # "找到、计算、赋值",找到的不是产品对象,而是一个数字。
               # product_stock 里存的是数量,产品对象存在 catalog 里,这是两个字典。
               self.product_stock[name] -= quantity
               # step A: look up the product object by name                 
               # step B: ask THAT object for its price
               unit_price = self.catalog[name].unit_price()
               subtotal = unit_price * quantity
               total += subtotal
               lines.append({"name": name, "quantity": quantity, "unit_price": unit_price, "subtotal": subtotal})
          return {"lines": lines, "total": total}
               
          

     def pending_requests(self):               
          return dict(self.requests)





     
          
