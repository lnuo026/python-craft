
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
