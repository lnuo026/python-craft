import json 
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "demo_data"
DATA_DIR.mkdir(exist_ok=True)

def section(number, title):
     print(f"\n--- {number}, {title} ---")

# write, append, read
def demo_text_file():
     path = DATA_DIR / "notes.txt"

     # "w" 
     with open(path, "w", encoding="utf-8") as f:
          f.write("line one\n")
          f.write("line two\n")

     # "a"
     with open(path, "a", encoding="utf-8") as f:
          f.write("Hi,this is append function\n")

     # "r"
     with open(path, "r", encoding="utf-8")as f:
          print("read: ", repr(f.read()))



# JSON and python转换
def demo_json_strings():
     pet = {"name": "Rex", "age": 4, "vaccinated": True, "owner": None, "tags": ["dog", "friendly"]}
     text = json.dumps(pet)
     print("dump: ", text)
     print()
     # indent 就是"缩进"的意思,2 表示每深入一层,缩进 2 个空格。
     print(json.dumps(pet, indent=2))
     print()
     back = json.loads(text)
     print("loads", back, type(back).__name__)
     print()


# 把数据存进文件,再读回来
def demo_json_files():
     path = DATA_DIR / "dump.json"
     pets = [
          {"species": "dog", "name": "Rex", "age": 4, "temperature": 39.8},
          {"species": "cat", "name": "小白", "age": 2, "mood": "calm", "temperature": 39.2}
     ]
     with open(path, "w", encoding="utf-8") as f:
          # ensure_ascii=False 的作用是让非英文字符(比如中文)在 JSON 文件里原样保存,不被转成转义码
          json.dump(pets, f, indent=2, ensure_ascii=False)
     
     print("file content: ", path.read_text(encoding="utf-8"))

     with open(path, encoding="utf-8")as f:
          loaded = json.load(f)
          # len()列表最外层的元素个数,这里是 2
     print("loaded", len(loaded))
     print(loaded == pets)



if __name__ == "__main__":
     demo_text_file()
     demo_json_strings()
     demo_json_files()

