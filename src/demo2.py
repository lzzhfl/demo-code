import time
from llama_index.core.llms import ChatMessage
from llama_index.llms.deepseek import DeepSeek
llm = DeepSeek(model="deepseek-chat", api_key="sk-5c61862e793647d0986e1d9c25aef818")

# 方式一：直接调用 complete 方法
# response = llm.complete("解释低延迟大语言模型的重要性")
# print(response)

# 方式二：流式调用 stream_complete 方法
# response = llm.stream_complete("你好")
# for chunk in response:
#     # print("类型:", type(chunk))
#     # print("repr:", repr(chunk))    # 对象原始显示 
#     # time.sleep(0.3)
#     print(chunk.delta, end='', flush=True)


# 方式三：多轮会话调用 chat 方法
# messages = [
#     ChatMessage(role="user", content="你好")
# ]

# response = llm.chat(messages)
# print(type(response))
# print(repr(response))
# print(response)  # 
# print(response.message.role)
# print(response.message.content)

# 方式四：多轮会话流式调用 stream_chat 方法，包含历史消息
messages = [
    ChatMessage(role="user", content="你好")
]


response = llm.stream_chat(messages)
print(type(response))
print(repr(response))
for chunk in response:
    print(repr(chunk))
    print(chunk.delta, end='', flush=True)