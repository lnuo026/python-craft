import asyncio
import time

async def fetch(name, seconds):
     await asyncio.sleep(seconds)
     return name


async def main():
     result = await fetch("a", 5)
     print(result)



# 定义不等于执行
async def m():
     result = await fetch(2, 1)
     print(type(result))



# 让多个任务一起等:gather 和 create_task
# time 是 Python 自带的一个模块
async def mutiple():
     start = time.perf_counter()
     # 连续写多个 `await` 是串行的,每个都要等前一个完成
     await fetch("a", 1)
     await fetch("b", 2)
     print(f"sequential: {time.perf_counter() - start:.1f}s")

     # `asyncio.gather(...)` 把多个协程一起交给事件循环,一起等   
     # gather 几个任务一起跑完，全部结束之后把结果给我
     start = time.perf_counter()
     results = await asyncio.gather(fetch("a", 1), fetch("b", 2), fetch("c", 2))
     print(results, f"results: {time.perf_counter() - start:.1f}s")


# create_task把一个协程立刻安排进事件循环,不阻塞当前代码,稍后再取结果。`gather` 内部就是这样做的
async def ct():
     task = asyncio.create_task(fetch("z", 1))
     print("doing other work while the task runs")
     print("task result", await task)


# 阻塞调用,写了 async def,不代表函数就不会卡住别人,关键看函数里面做的事。
#  asyncio.to_thread + 普通time.sleep()
def slow_job(name):
     time.sleep(1)
     return name

async def blocking_fetch(name, seconds):
     time.sleep(seconds)
     return name

async def function_actual_call():
     start = time.perf_counter()
     await asyncio.gather(fetch("a", 1), fetch("c", 1), fetch("b", 1))
     print(f"asynico x3: {time.perf_counter() - start:.1f}s\n")

     start = time.perf_counter()
     await asyncio.gather(blocking_fetch("a", 1), blocking_fetch("c", 1), blocking_fetch("b", 1))
     print(f"time.sleep x3: {time.perf_counter() - start:.1f}s \n")

     start = time.perf_counter()
     await asyncio.gather(
          asyncio.to_thread(slow_job, "a"), 
          asyncio.to_thread(slow_job, "b"),
          asyncio.to_thread(slow_job, "c")
          )
     print(f"to_thread x3: {time.perf_counter() - start:.1f}s\n")




# exception
async def bad_fetch():
     await asyncio.sleep(0.1)
     raise ValueError("boom")

async def exceptions():
     try:
          await bad_fetch()
     except ValueError as e:
          print("caught", e)
     # `return_exceptions=True` 是 `asyncio.gather(...)`
     result = await asyncio.gather(fetch("a", 0.2), bad_fetch(), return_exceptions=True)
     # print:
     # caught boom
     # ['a', ValueError('boom')]
     print(result)
     print(result[0])
     print(result[1])
     print(type(result[1]))


# async with 和 async for
class Connection:
     async def __aenter__(self):
          print("open connection")
          return self

     async def __aexit__(self, exc_type, exc, tb):
          print("close connection")
          return False

async def async_with_for():
     async with Connection() as c:
          print("working inside the with block")



     
# `asyncio.run(main())` 这是整个程序真正开始的地方
asyncio.run(async_with_for())