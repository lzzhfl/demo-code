from llama_index.embeddings.openai_like import OpenAILikeEmbedding
import os
from dotenv import load_dotenv

load_dotenv()
SILICONFLOW_BASE_URL = os.getenv("SILICONFLOW_BASE_URL") # 从 .env 读
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")   # 从 .env 读

embed_model = OpenAILikeEmbedding(
    model_name="BAAI/bge-m3",  # 硅基流动支持的嵌入模型
    api_base=SILICONFLOW_BASE_URL,
    api_key=SILICONFLOW_API_KEY,
)

# get_query_embedding 问题向量转换
query_emb = embed_model.get_query_embedding('你好')
print(query_emb)

# 文档向量转换
# text_emb = embed_model.get_text_embedding('你好')
# print(text_emb)

# 批量处理
# text_emb = embed_model.get_text_embedding_batch(['你好', '你好'])
# print(text_emb)