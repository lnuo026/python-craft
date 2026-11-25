history_by_session = {}
# user send two messages and retrives , {}


# Gemini 要求一条消息把「谁说的」放在 role 里，把「说了什么」放在 parts 里
def make_message(role, text):
     return {"role": role, "parts":[{"text": text}]}


def add_message(session_id, role, text):
     if session_id not in history_by_session:
          history_by_session[session_id] = []

     message = make_message(role, text)
     
     # history_by_session[session_id] = [] 是一次字典赋值
     # history_by_session[7] = []  --> {7: []}:7 号会话已经建好，目前有零条消息。
     history_by_session[session_id].append(message)


def get_history(session_id):
     if session_id not in history_by_session:
          return []     
     return history_by_session[session_id]
     

# if __name__ == "__main__":
#      add_message(7, "hammer", "First message")
#      add_message(7, "bean", "Second message")
#      print(get_history(7))
#      print(get_history(8))

     
