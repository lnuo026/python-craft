def shout(func):
     def machine(n):
          return func(n).upper()
     return machine





def hi(name):
     return f"hello, {name}"

Hello = shout(hi)
print(Hello("mike"))
print()


@shout
def hey(na):
     return f"hhhhhey, {na}"

print(hey("SSSSam"))


print(f"origin (Hi)function: {hi("mike")}")
print(f"origin (hey:不能再用名字直接调用)function: {hey("Sam")}")