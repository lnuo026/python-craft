def gr(name):
     return f"hello, {name}"

def gr_shout(n):
     return gr(n).upper()

print(gr("bean"))
print(gr_shout("kitty"))
print()


# call_of 被调用时,立刻去执行了 func(name),返回的是一个结果(字符串)。
# 而装饰器不立刻执行,它只接收原函数,返回一个新函数,等以后有人调用那个新函数时,才去执行。(返回一台"机器")
# 把 gr_shout 里写死的 gr,换成一个参数,谁来决定调用哪个函数,由调用者传进来
def bye (name):
     return f"goodbye, {name}"
def gr(name):
     return f"hello, {name}"

def gr_shout(n):
     return gr(n).upper()

print(gr("bean"))
print(gr_shout("kitty"))
print()


# call_of 被调用时,立刻去执行了 func(name),返回的是一个结果(字符串)。
# 而装饰器不立刻执行,它只接收原函数,返回一个新函数,等以后有人调用那个新函数时,才去执行。(返回一台"机器")
# 把 gr_shout 里写死的 gr,换成一个参数,谁来决定调用哪个函数,由调用者传进来
def bye (name):
     return f"goodbye, {name}"

# 它有两个接收口,func 收函数,name 收数据。
# 函数体里 func(name).upper(),就是调用传进来的那个函数,再把结果变大写。
# 传 gr 进去,它就先调 gr;
# 传 bye 进去,它就先调 bye。shout_of 自己一行没改,就能给任何函数都"套上变大写的外壳"。
def call_of(func, name):
     return func(name).upper()

print(call_of(gr, "Jam"))
print(call_of(bye, "Mike"))
print()


# but call_of is not decorator yet;
# 只改一个地方:让它不要立刻执行,而是返回一台"机器"
# machine 是在 make_shouter 里面定义的一个函数,
# make_shouter 最后 return machine,
# 注意后面没有括号,返回的是函数本身。
def make_shouter(func):
     def machine(name):
          return func(name).upper()
     return machine

# 这一行只造出了机器,还没有开始做 hello
shout_gr = make_shouter(gr)
# 等到 shout_gr("Tom"),机器才开始工作。shout_gr("Ann") 再按一次。
# call_of(gr, "Tom") 每次都要把函数和名字一起传;
# shout_gr("Tom") 只需要传名字,"调用哪个函数"已经被机器记住了
print(shout_gr("Tom"))
print(shout_gr("Ann"))


# 它有两个接收口,func 收函数,name 收数据。
# 函数体里 func(name).upper(),就是调用传进来的那个函数,再把结果变大写。
# 传 gr 进去,它就先调 gr;
# 传 bye 进去,它就先调 bye。shout_of 自己一行没改,就能给任何函数都"套上变大写的外壳"。
def call_of(func, name):
     return func(name).upper()

print(call_of(gr, "Jam"))
print(call_of(bye, "Mike"))
print()


# but call_of is not decorator yet;
# 只改一个地方:让它不要立刻执行,而是返回一台"机器"
# maek_shouter: "机器模板",'装饰器' the decorator: the template that builds machines
# 包装函数(wrapper)	machine	模板造出来的机器,里面会调用原函数
# make_shouter 最后 return machine,
# 注意后面没有括号,返回的是函数本身。
def make_shouter(func):
     def machine(name):
          return func(name).upper()
     return machine

# gr 原函数(被装饰的函数)
# 这一行只造出了机器,还没有开始做 hello
# 是装饰后的函数 shout_gr	存着那台机器的变量,真正被调用的就是它
shout_gr = make_shouter(gr)
print(shout_gr)
# 等到 shout_gr("Tom"),机器才开始工作。shout_gr("Ann") 再按一次。
# call_of(gr, "Tom") 每次都要把函数和名字一起传;
# shout_gr("Tom") 只需要传名字,"调用哪个函数"已经被机器记住了
print(shout_gr("Tom"))
print(shout_gr("Ann"))
# 每次调用 make_shouter(gr),造出来的都是一个新的、不同的函数,两次得到的互相不是同一个
print(shout_gr(gr) is shout_gr(gr))



