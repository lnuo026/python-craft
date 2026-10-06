# [dog, cat 全部自动list ，然后循环检查， 该包导入main， 直接输出]
# 工厂函数 + 批量检查函数

from app.dog.hammer import dog
from app.cat.kitty import cat

def build_pet(raw_date):
     pets = []
     for item in raw_date:
          if item["species"] == "dog":
               # 在"造一个新的 dog 对象"，和之前手写的 s3 = dog("hammer", 10, 39.1) 是同一个动作,只是这次参数不是直接写死的值,从 item 这个 dict 里现查出来的
               pets.append(dog(item["name"], item["age"], item["temperature"]))
          elif item["species"] == "cat":
               pets.append(cat(item["name"], item["age"], item["mood"], item["temperature"]))
     return pets


def check_all_pets(pets):
          for pet in pets:
               status = "emergency" if pet.is_emergency() else "observe"
               print(f"{pet.name} -> {status}")



# "这个对象到底是什么类型"的工具,叫 isinstance(i, object):
def all_detail(pets):
      for i in pets:
          if isinstance(i, cat):
               print(f"cat: {i.name, i.age, i.mood, i.temperature}")
          else:
                print(f"dog: {i.name, i.age, i.temperature}")
            




