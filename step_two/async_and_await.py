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


# 阻塞调用

     
# `asyncio.run(main())` 这是整个程序真正开始的地方
asyncio.run(ct())