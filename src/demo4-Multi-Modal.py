import os
from dotenv import load_dotenv

load_dotenv()
SILICONFLOW_BASE_URL = os.getenv("SILICONFLOW_BASE_URL") # 从 .env 读
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")   # 从 .env 读

from llama_index.llms.openai_like import OpenAILike
from llama_index.core.prompts import RichPromptTemplate

multi_modal_template_str = """
{% chat role="system" %}
  你是一个专业的图像处理专家，请仔细观察图片内容，回答用户问题。
{% endchat %}

{% chat role="user" %}
    {% for image_path in image_paths %}
        图片{{loop.index}}:{{image_path | image}}
    {% endfor %}
    用户问题：{{query_str}}
    请用中文回答，并分别描述每张图片的关键内容，最后总结他们的共同点。
{% endchat %}

"""
multi_modal_template = RichPromptTemplate(multi_modal_template_str)
messages = multi_modal_template.format_messages(
    image_paths=[
        "src/data_file/img.png",
        "src/data_file/img_1.png"
    ],
    query_str="这些图片里有什么共同点？"
)
print(messages)

# Settings 是 LlamaIndex 中非常重要的全局配置对象（singleton 单例模式）。
# 它的作用是：为整个应用提供默认的 LLM、Embedding、文本切分器等组件。 一旦设置，后续的 组件如果没有显式传入对应参数，就会自动使用 Settings 中的配置。
# 1. 配置对话模型（LLM）
llm = OpenAILike(
    model='Qwen/Qwen3-Omni-30B-A3B-Thinking',
    api_base=SILICONFLOW_BASE_URL,
    api_key=SILICONFLOW_API_KEY,
    is_chat_model=True,# 是否是 Chat Model
    context_window=32768,
)

res = llm.chat(messages)
print(res)