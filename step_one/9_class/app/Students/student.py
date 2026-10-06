class Student:
     def __init__(self, name, age):
          self.name = name
          self.age = age

s1 = Student("hammer", 3)

# __init__里面的参数必须要完整
# s2 = Student("bean") x

print(s1.name, s1.age)


# or 默认值
class Student:
     def __init__(self, name, age=0):
          self.name = name
          self.age = age

# __init__里面的参数不完整，有default
s2 = Student("bean") 
print(s2.name, s2.age)


# self 指向同一个对象,而这个对象身上挂着的属性(通过 self.xxx = ... 存的)能跨方法持续存在
class S:
     def __init__(self, name):
          self.name = name
     
     def greet(self):
          print(f"Hi, {self.name}")
s3 = S("H")
s3.greet()

# 内部的局部变量,函数跑完就消失了
class SS:
     def __init__(self, name):
          self.name = name
          local_var = "temp"
          self.name = local_var +" "+name
          print(local_var)
          
s4 = SS("L")
print(s4.name)


# 出去：local var 挂在 self 上
class SSS:
     def __init__(self, name):
          self.name = name
          local_var = "Hi"
          self.saved_var = local_var

     def greet(self):
          print(self.saved_var+ " " + self.name)
          
          
s5 = SSS("beannn")
s5.greet()
print()

# 出去：local var return
# 不存在这种使用（很少）


# __init__
# calculation
class numberss:
     def __init__(self, temperature):
          self.temperature = temperature
          self.is_emergency = temperature > 40

p1 = numberss(45)
# 错误 print(p1.numberss()) 对象身上不会自动多出一个和类同名的方法
print(p1.is_emergency)
print()
          

# 可以配合 `**kwargs` 灵活接收数量不定的字段
class Pet:
     def __init__(self, name, **extra_info):
          self.name = name
          self.extra_info = extra_info

p1 = Pet("hammer", breed="labrador", age=5, weight=25)
print(p1.extra_info)
print()


from app.People.people import person
class studing(person):
     def __init__(self, name, age, scores):
          super().__init__(name)
          self.age = age
          self.scores = scores
     def show_detail(self):
          print(self.name, self.age, self.scores)

     # __str__: print 这个对象,改写内容
     def __str__(self):
          return f"this student is: {self.name}"

# "调用父类 person 的 greet 方法,并把结果原样返回"
     def greet(self):
          return super().greet()

# change
     def greet(self):
          print(f"Hi, My age is {self.age}")

