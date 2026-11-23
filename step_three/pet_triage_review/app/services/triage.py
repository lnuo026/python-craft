

def parse_triage(raw):
     if "[TRIAGE:RED]" in raw:
          level = "red"
     elif "[TRIAGE:YELLOW]" in raw:
          level="yellow"
     elif "[TRIAGE:GREEN]" in raw:
          level="green"
     else:
          level="unknown"

     # strip()去掉字符串首尾的空白，中间的空格保留
     # raw 是整段原文，而 tag 表示你想从原文里删掉的那一小段
     clean_text = raw.strip()
     if level != "unknown":
          #  需要upper()因为.replace() 要先找到完全一样的文字，才能把它删掉
          tag = f"[TRIAGE:{level.upper()}]"
          # 文字.replace(旧文字, 新文字),把文字中匹配的部分换掉;
          # clean_text存的是正文对话, 需要去掉Triage这个标签
          clean_text = raw.replace(tag, "").strip()

     return {"triage_level": level, "clean_text": clean_text}

print(parse_triage("[TRIAGE:GREEN]"))
print(parse_triage("[TRIAGE:BLUE]"))
print(parse_triage("[TRIAGE:BLUE]  unknown   "))

