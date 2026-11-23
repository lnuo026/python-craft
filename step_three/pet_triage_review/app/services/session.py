history_by_session = {}
# user send two messages and retrives , {}

def add_message(session_id, role, text):
     if session_id not in history_by_session:
          history_by_session[session_id] = []

     message = {"role": role, "part": [{"text": text}]}
     
     # history_by_session[session_id] = [] 是一次字典赋值
     # history_by_session[7] = []  --> {7: []}:7 号会话已经建好，目前有零条消息。
     history_by_session[session_id].append(message)


def get_history(session_id):
     if session_id not in history_by_session:
          return []     
     return history_by_session[session_id]
     

if __name__ == "__main__":
     add_message(7, "hammer", "First message")
     add_message(7, "bean", "Second message")
     print(get_history(7))
     print(get_history(8))

     
