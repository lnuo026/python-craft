def greeting(name):
     return f"hello, {name}"

say = greeting
print(say("hammer"))
print(greeting)
print(say)
print(say is greeting)
print()

# :函数可以作为参数,传给另一个函数。
def run_twice(function_as_paramter, normal_parameter):
     return [function_as_paramter(normal_parameter), function_as_paramter(normal_parameter)]



# 传进去的是 greeting,后面没有括号,所以传的是函数本身,不是执行它的结果
print(run_twice(greeting, 'bean'))
print()


# 函数里面可以定义函数,还能把它返回
def make_greeter(prefix):
     def inner(name):
          return f"{prefix}, {name} \n"
     return inner

hi = make_greeter("Hi")
print(hi("hammer"))


# 装饰器就是:接收一个函数,返回一个包装过的新函数,装饰器之所以能成立,前提是函数本身可以被当作一个东西,传给另一个函数去处理
def greet(name):
     return f"hello, {name}"


# func 原来的函数,比如 gr,调用 shout(greeting) 时传进来的
# wrapper	新函数,外壳 shout 里面自己定义出来的
def shout(func):
     print("shout is running, func is", func.__name__)

     def wrapper(n):
          print("wrapper is running, name is", n)
          return func(n).upper()
     
     return wrapper

loud = shout(greet)
print(loud("bean"))
print(loud("kitty"))
print(greet("bean"))
print()

# 装饰器里的 wrapper(*args, **kwargs),意思是"不管被包装的函数需要什么参数,我都先全部收下"。
# 收下之后,再用 func(*args, **kwargs) 原样递给原函数。
# def shout(func):
#      def wrapper(*args, **kwargs):
#           result = func()
