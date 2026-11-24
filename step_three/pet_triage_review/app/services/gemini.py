from google import genai


def call_gemini(contents):
     # Client` 是genai 里面的类
     # 进入下面这段代码时，准备好资源；离开这段代码时，自动收尾。
     # Python 先取出回复文字，退出 with 时关闭客户端，再把文字交给调用方
     with genai.Client() as client:
          response = client.models.generate_content(
               model="gemini-3.5-flash",
               contents=contents,
          )
          return response.text
