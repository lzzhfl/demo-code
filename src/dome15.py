from llama_index.core.node_parser import SentenceSplitter

from base_llm import llm, embed_model
from llama_index.core import SimpleDirectoryReader
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core.vector_stores.types import VectorStoreQuery

from llama_index.core import StorageContext

# 加载文档
documents = SimpleDirectoryReader(input_files=["src/data_file/小说.txt"]).load_data()
print("-------------------使用最基础的内存向量进行本地存储----------------------")
nodes = SentenceSplitter(
    chunk_size=500,
    chunk_overlap=50
).get_nodes_from_documents(documents)

# # 创建一个最基础的内存向量
vector_store = SimpleVectorStore()
# # 创建一个存储容器
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# 持久化保存
storage_context.persist("./storage")
# print(storage_context.vector_store.data)

# # 批量生成 embedding
for node in nodes:
    node.embedding = embed_model.get_text_embedding(node.text)

# 写入 VectorStore
storage_context.vector_store.add(nodes)
storage_context.docstore.add_documents(nodes)


# 构建查询对象
query_embedding = embed_model.get_query_embedding('萧炎的父亲是谁?')
query = VectorStoreQuery(
    query_embedding=query_embedding,
    similarity_top_k=3
)

result = storage_context.vector_store.query(query)
print(f"查询: 萧炎的父亲是谁?\n")

context_parts = []
for node_id, similarity in zip(result.ids, result.similarities):
    node = storage_context.docstore.get_node(node_id)
    context_parts.append(node.text)

# ====== 生成部分（新增）======
context_str = "\n\n".join(context_parts)
response = llm.complete(
    f"根据以下上下文，用中文回答问题。\n\n上下文：\n{context_str}\n\n问题：萧炎的父亲是谁？"
)
print(f"\n=== LLM 回答 ===\n{response}")

