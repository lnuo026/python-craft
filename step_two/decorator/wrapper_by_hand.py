def gr(name):
     return f"hello, {name}"

def gr_shout(n):
     return gr(n).upper()

print(gr("bean"))
print(gr_shout("kitty"))
print()

# 把 gr_shout 里写死的 gr,换成一个参数,谁来决定调用哪个函数,由调用者传进来
def bye (name):
     return f"goodbye, {name}"

def call_of(func, name):
     return func(name).upper()

print(call_of(gr, "Jam"))
print(call_of(bye, "Mike"))