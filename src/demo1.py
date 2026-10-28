import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
SILICONFLOW_BASE_URL = os.getenv("SILICONFLOW_BASE_URL") # 从 .env 读
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")   # 从 .env 读

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.openai_like import OpenAILikeEmbedding

# Settings 是 LlamaIndex 中非常重要的全局配置对象（singleton 单例模式）。
# 它的作用是：为整个应用提供默认的 LLM、Embedding、文本切分器等组件。 一旦设置，后续的 组件如果没有显式传入对应参数，就会自动使用 Settings 中的配置。
# 1. 配置对话模型（LLM）
Settings.llm = OpenAILike(
    model="Qwen/Qwen2.5-7B-Instruct",  # 可换成 deepseek-ai/DeepSeek-V3 等
    api_base=SILICONFLOW_BASE_URL,
    api_key=SILICONFLOW_API_KEY,
    is_chat_model=True,# 是否是 Chat Model
    context_window=32768,
)

# 2. 配置嵌入模型（Embedding）
# 硅基流动也提供 OpenAI 兼容的嵌入接口
Settings.embed_model = OpenAILikeEmbedding(
    model_name="BAAI/bge-m3",  # 硅基流动支持的嵌入模型
    api_base=SILICONFLOW_BASE_URL,
    api_key=SILICONFLOW_API_KEY,
)
from pathlib import Path
# ========== 使用区 ==========
# 3. 加载文档（准备一个 ./data 文件夹放你的文件）
# 1.加载本地文档
data_dir = Path(__file__).parent / "data"
docs = SimpleDirectoryReader(data_dir).load_data()

# 4. 建索引
index = VectorStoreIndex.from_documents(docs)

# 5. 查询
query_engine = index.as_query_engine()
response = query_engine.query("ssq是什么？")
print(response)

print("\n--- 来源节点 ---")
for node in response.source_nodes:
    print(f"相似度: {node.score:.4f} | 文件: {node.metadata.get('file_name')}")