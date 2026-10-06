# bakery 3 tests
# not enough ingredients
# unknown product
# invalid quantity

import unittest
from app.exceptions import InsufficientIngredients, UnknownProduct, OutOfstock
from app.product.bakery import Bakery
from app.product.breads import Breads
from app.product.cake import Cake

class TestBake(unittest.TestCase):
     def setUp(self):
          # runs before every test: a fresh bakery each time
          # 创建一个面包店,起始原料是面粉 1000、糖 100、黄油 100。
          # 存到 self.bakery 上,这样本类里的所有测试方法都能通过 self.bakery 用到它。
          # setUp 保证每个测试开始时,都是一个全新的、数字相同的面包店。
          self.bakery = Bakery({"flour": 1000, "sugar": 100, "butter": 100})
          self.bakery.register(Breads("white bread", 10, {"flour": 300, "sugar": 20, "butter": 30}, "white"))

     # 方法名以 test_ 开头,unittest 才会把它当作测试自动运行
     def test_bake_success(self):
          # 烘焙 2 个白面包，消耗了flour 600,多出来2 个 white bread
          self.bakery.bake("white bread", 2)
          # 断言:面粉库存应该等于 400。
          # assertEqual(a, b) 检查 a 和 b 是否相等,相等就继续,不相等测试就失败,并显示两边的值。
          # 400 的来源:起始 1000,2 个面包需要 300 × 2 = 600,剩下 400。
          self.assertEqual(self.bakery.ingredients["flour"], 400)
          self.assertEqual(self.bakery.product_stock["white bread"], 2)
     
     
     # 测试原料不够,而且库存没变,先检查、再扣减":失败时,没有任何原料被扣掉
     def test_not_enough_ingredients(self):
          # dict(...) 复制了一份库存,用来和失败后的库存比较。
          # 如果直接写 before = self.bakery.ingredients,两个名字指向的是同一个字典,后面库存如果被改动,before 也会跟着变
          before = dict(self.bakery.ingredients)
          # with self.assertRaises(某异常): 表示"里面这段代码必须抛出这种异常",没抛出来就算失败;抛出别的异常也失败
          with self.assertRaises(InsufficientIngredients):
               # 100 个白面包需要面粉 30000,远超库存,所以应该抛这个异常。
               self.bakery.bake("white bread", 100)
          # 断言:烘焙失败之后,库存和之前的快照完全一样,写在 with 外面,是因为 bake 抛异常后就离开了 with 块
          self.assertEqual(self.bakery.ingredients, before)



     def test_unknown_product(self):
          with self.assertRaises(UnknownProduct):
               self.bakery.bake("pizza", 1)
          
     def test_invalid_quantity(self):
          with self.assertRaises(ValueError):
               self.bakery.bake("white bread", -1)




class TestOrder(unittest.TestCase):
     def setUp(self):
          self.b = Bakery({"flour": 5000, "sugar": 1000, "butter": 800, "eggs": 30})
          # 登记两种面包到目录里。登记不带数量,所以它们的成品库存此时都是 0
          self.b.register(Breads("white bread", 10, {"flour": 300, "sugar": 20, "butter": 30}, "white"))
          self.b.register(Breads("black bread", 20, {"flour": 110, "sugar": 30, "butter": 25}, "black"))
          # 烘焙 3 个白面包,白面包成品库存变成 3。黑面包没有烘焙,库存保持 0,这是后面"某一行库存不够"的测试要用到的。
          self.b.bake("white bread", 3)

     def test_order_success(self):
          receipt = self.b.order({"white bread": 2})
          # 断言总价是 20,2 个白面包乘以单价 10,没错
          self.assertEqual(receipt["total"], 20)
          # 断言白面包库存从 3 变成 1,没错。
          self.assertEqual(self.b.product_stock["white bread"], 1)

     
     def test_one_line_short_changes_nothing(self):
          with self.assertRaises(OutOfstock):
               # 订单里黑面包库存是 0,不够,应该抛 OutOfstock。
               self.b.order({"white bread": 1, "black bread": 1})
          # 断言整单被拒绝之后,白面包库存还是 3,没有被扣。这是整个阶段最核心的那条检查。
          self.assertEqual(self.b.product_stock["white bread"] ,3)


     def test_unknown_product_changes_nothing(self):
          with self.assertRaises(UnknownProduct):
               # 放一个已登记的产品和一个未登记的产品混在一起,才能验证"部分有效的订单也整单拒绝"
               self.b.order({"white bread": 1, "pizza": 1})
               # 断言白面包库存没变。
          self.assertEqual(self.b.product_stock["white bread"], 3)

     def test_invalid_quantity_changes_nothing(self):
          with self.assertRaises(ValueError):
               # 黑面包数量是 -1,不是正整数,应该抛 ValueError
               self.b.order({"white bread": 1, "black bread": -1})
          # 断言白面包库存没变。
          self.assertEqual(self.b.product_stock["white bread"], 3)


     def test_polymorphic_price(self):
          self.b.register(Cake("small cake", 15, {"flour": 100, "sugar": 200, "butter": 180, "eggs": 4}, 2))
          # 烘焙 1 个小蛋糕
          self.b.bake("small cake", 1)
          # 一张订单里同时买一种面包和一种蛋糕。
          receipt = self.b.order({"white bread": 1, "small cake": 1 })
          # 检查蛋糕的价格走的是它自己的计价方法
          self.assertEqual(receipt["total"], 10 + 55)


     def test_unknow_product_is_record(self):
          with self.assertRaises(UnknownProduct):
               # 下单一个没有的产品,抛异常后,需求记录里应该有 pizza 被问过 1 次
               self.b.order({"pizza": 1})
          self.assertEqual(self.b.pending_requests(), {"pizza": 1})
          with self.assertRaises(UnknownProduct):
               # 再下一次,记录变成 2 次。这个测试这次通过
               self.b.order({"pizza": 2})
          self.assertEqual(self.b.pending_requests(), {"pizza": 2})



     def test_registering_clears_the_request(self):
          with self.assertRaises(UnknownProduct):
               self.b.order({"rye bread": 1})
          self.b.register(Breads("rye bread", 12, {"flour": 250}, "rye"))
          # 登记黑麦面包之后,需求记录应该清空
          self.assertEqual(self.b.pending_requests(), {})

          



if __name__ == "__main__":
     unittest.main()