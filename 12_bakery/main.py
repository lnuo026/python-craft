from app.product.breads import Breads
from app.product.cake import Cake
from app.product.bakery import Bakery

# self, name, price, recipe, kind
# (self, name, price, recipe, layer):
Items = [
    Breads("white bread", 10, {"flour": 300, "sugar": 20, "butter": 30}, "white"),
    Breads("black bread", 20, {"flour": 110, "sugar": 30, "butter": 25}, "black"),
    Cake("small cake", 15, {"flour": 100, "sugar": 200, "butter": 180, "eggs": 4}, 2),
    Cake("big cake", 30, {"flour": 200, "sugar": 150, "butter": 120, "eggs": 2}, 3),
]



total_stocks = Bakery({"flour": 5000, "sugar": 1000, "butter": 800, "eggs": 30})

for p in Items:
     total_stocks.register(p)
     print(p.describe())


total_stocks.bake("white bread", 2)
# ??ingredients 如何定义的？ 只有一个self
print(f"total_stocks.ingredients, {total_stocks.ingredients} \n") 
print(total_stocks.product_stock)
print()

bread = Items[0]
print(f"{bread.recipe} \n")
print(f"{bread.recipe.items()} \n")

# 想一次性看所有产品的配方,就需要两层循环,外层遍历列表,内层遍历每个产品的配方
for product in Items:
     for i, j in product.recipe.items():
          print(product.name, i, j)