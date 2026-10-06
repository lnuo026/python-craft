import logging
# 对日志系统做一次全局的基础配置。level=logging.INFO 表示只处理 INFO 及以上级别的日志(级别从低到高是 DEBUG、INFO、WARNING、ERROR、CRITICAL)。format 规定每条日志长什么样:%(levelname)s 会替换成级别名,%(message)s 替换成日志内容,所以最后输出像 ERROR: conversion failed。
logging.basicConfig(level = logging.INFO, format="%(levelname)s: %(message)s")
# 一个 logger 对象,以后用它记录日志。__name__ 是当前模块的名字,第八课讲过,直接运行这个文件时它的值是 "__main__"
logger = logging.getLogger(__name__)

# 小工具函数,用来在输出里打印每一节的标题
def printool(number, title):
     print(f"\n--- {number}, {title} ---")


# 1. An unhandled exception stops the program and prints a traceback.
# Uncomment the line at the bottom of this file (inside the __main__ block) to see it.



# 2. try / except
def demo_basic():
     try:
          # 想把字符串 "abc" 转成整数,但它不是数字,Python 抛出 ValueError。
          int("abc")
     except ValueError:
          print("not a valid number, caught ValueError, program continues")
          # 最后一个 print 比 except 少缩进一级,在 try/except 之外,不管有没有出错都会执行,说明程序没有被中断
     print("this line still runs")

# 3. several except blocks, and a tuple of types
def demo_multiple_except():
     data = {"name": "Rex"}
     for action in ("missing key", "divide", "bad index"):
          try:
               if action == "missing key":
                    # 取字典里不存在的键,抛 KeyError
                    data["age"]
               elif action == "divide":
                    # 10 / 0 抛 ZeroDivisionError。
                    10 / 0
               else:
                    # 把"创建列表"和"按下标取值"写在了同一行里 
                    # numbers = [1, 2, 3]
                    # numbers[10]
                    # [1, 2, 3] 是一个列表字面量,Python 执行到这里就会在内存里造出这个列表。紧跟着的 [10] 是下标取值,意思是取这个列表里下标为 10 的元素。
                    # 两对方括号虽然长得一样,但作用不同:前一对是"创建列表",后一对是"取元素"。
                    [1, 2, 3][10]
          # 三个 except 从上往下找第一个匹配的。前两个各处理一种异常,第三个用元组一次处理两种。
          except KeyError:
               print(f"{action}: KeyError")
          except ZeroDivisionError:
               print(f"{action}: ZeroDivisionError")
          except (IndexError, TypeError):
               print(f"{action}: IndexError or TypeError")

# 4. except ... as e,as e: 把捕获到的异常对象存进变量 e
def demo_as_e():
     try:
          int("abc")
     except ValueError as e:
          print("message: ", e)
          print("type: ", type(e).__name__)


# else 和 finally
def demo_else_finally(text):
     try:
          value = int(text)
     except ValueError:
          # f-string 中的 !r 表示用 repr 的方式显示,字符串会带上引号,这样能看出它是个字符串
          print(f"{text!r}: bad input")
     else:
          print(f"{text!r}: converted to {value}")
     finally:
          print("finally always runs")

# 主动抛出异常:raise
def set_temperature(value):
     if not isinstance(value, (int, float)):
          raise TypeError("temperature must be a number")
     if value < 30 or value > 45:
          raise ValueError("temperture out of range")
     return value


# 自定义异常:继承 Exception
class InvalidPetData(Exception):
# pass 表示"什么都不加",这个类不需要任何额外内容,它的名字本身就表达了含义
     pass

def validate_pet(item):
     if "name" not in item:
          raise InvalidPetData("no name")
     return item

def demo_user():
     try:
          validate_pet({"specise": "dog"})
     except InvalidPetData as e:
          print("InvaliPetData: ", e)


# assert
def demo_assert(temperture):
     try:
          assert temperture > 0, "temperture must be positive"
     except AssertionError as e:
          print("assertion failed: ", e)



# logging 模块recording
def demo_logging():
     try:
          int("abc")
     except ValueError:
          logger.exception("conversion failed")



# mian run
def demo_raise():
     for v in (38.5, "39", 99):
          try:
               print("accepted:", set_temperature(v))
          except(TypeError, ValueError) as e:
               print(f"rejected {v!r}: {e}")

def main():
     printool(2, "try / except")
     demo_basic()
     printool(3, "severval  except blocks")
     demo_multiple_except()
     printool(4, "as e")
     demo_as_e()
     printool(5, "else / finally")
     demo_else_finally("42")
     demo_else_finally("x")
     printool(6, "raise for validation")
     demo_raise()
     printool(7, "user exception")
     demo_user()
     printool(8, "assert")
     demo_assert(1)
     demo_assert(-2)
     printool(9, "logging")
     demo_logging()

     # printool(2, "try / except")
     

if __name__  == "__main__":
     main()
