
# `os` 用来读环境变量,os.environ 时，就是通过名字 os 找到这个模块，再用点号 . 访问它提供的环境变量。
# environ` 保存着当前程序能读到的环境变量，可以像字典一样按键查值。
import os

# `load_dotenv` 用来加载 .env 文件
# `MongoClient` 用来创建数据库客户端。
from dotenv import load_dotenv
from pymongo import  MongoClient

if __name__ == "__main__":
     load_dotenv("/Users/a11111/WorkSpace/python/agent/pet-triage/.env")
     mongo_uri = os.environ["MONGO_URI"]

     with MongoClient(mongo_uri, serverSelectionTimeoutMS=5000) as client:
          # result = database.command("ping")
          # client.admin 是对象，指 MongoDB 里名为 admin 的数据库。
          # command 是 PyMongo 提供的方法，用来执行数据库命令。
          # "ping" 是传给方法的字符串，指定要执行 MongoDB 的 ping 命令，检查服务器能否回应。
          result = client.admin.command("ping")
          print(result["ok"])

          database = client["pet_triage"]
          chat_logs = database["chat_logs"]
          record = {"sessionId": 1, "role": "user", "content": "hammer"}
          # `insert_one` 是 PyMongo 的集合方法，意思是“插入一份文档”。它返回写入结果
          # `.inserted_id` 从结果里取出这条记录的 ID，`print(...)` 把 ID 显示出来。
          print(chat_logs.insert_one(record).inserted_id)

          # = 表示默认值,调用时省略第四个参数
          # -> None 表示这个函数预期不返回业务数据,只做事情。
          #  : 表示函数体从下一行缩进处开始。
          async def log_message(sessionId: str, role: str, content: str, triage_level: str = "unknown") -> None:
               await log_message("91", "user", "something")
               await log_message("34", "assistant", "test reply", "yellow")





