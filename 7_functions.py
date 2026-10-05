def greet():
     print("Hi")

greet()

# parameter
def student_name(name, age):
     print(name, age)
     print(f"good for you,{name} !" )
     print(f"upper: {name.upper()}")

student_name("xiaohong", 13)
student_name(age=15, name="xiaolan")
print()


# 默认参数， 可以覆盖
def greet(name, greeting="morning"):
     print(f"{greeting}, {name} !")

greet("hammer")
greet("bean", "good afternoon")
print()



#  return value
# 不用必须声明返回类型
def add(a, b):
     return a + b

result = add(1, 3)
print(result)
print()



# *args —— 接收数量不固定的位置参数
def add_all(*numbers):
     total = 0
     for i in numbers:
          total += i
     return total

print(add_all(1, 2, 3))
print()

# 连锁指数运算,每个数的指数,是上一轮算出来的结果,
def expontial(*times):
     total = 0
     for i in times:
          temp = i
          total= i ** temp
     return total

print(f"上一轮结果次方：{expontial(1, 2, 3)}")
print()

# 自己的次方自己,1**1, 2**2, 3**3,再加起来
def expontial_v2(*numbers):
     total = 0
     for i in numbers:
          total += i ** i
     return total

print(f"自己的次方自己: {expontial_v2(1, 2, 3)}")




# **kwargs —— 接收数量不固定的关键字参数
def show_info(**info):
     print(info)

show_info(name="hammer", age=3, grade="A+")
print()



# 一次返回多个值
def get_min_max(numbers):
     return min(numbers), max(numbers)

low, high = get_min_max([3, 4, 5, 10])
print(low, high)


# 变量作用域(scope)——函数内外互不干扰
def my_func():
     x = 100
     print(x)

my_func()
# print(x) NameError，函数外面根本不认识这个 x


# 没有 return 的函数,默认返回 None
def say_hi():
     print("Hi")
     return "Hi"

result = say_hi()
print(result)
