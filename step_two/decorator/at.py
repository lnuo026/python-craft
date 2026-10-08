def shout(func):
     def machine(n):
          return func(n).upper()
     return machine





def hi(name):
     return f"Hi, {name}"

Hi = shout(hi)
print(Hi("mike"))
print()


@shout
def hey(na):
     return f"hey, {na}"

print(hey("Sam"))


print(f"origin (Hi)function: {hi("mike")}")
print(f"origin (hey:不能再用名字直接调用)function: {hey("Sam")}")