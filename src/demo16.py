from base_llm import llm, embed_model
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

import chromadb

# 加载文档
documents = SimpleDirectoryReader(input_files=["src/data_file/小说.txt"]).load_data()

print("---------------使用chroma进行存储向量--------------------")
# 创建客户端和新的集合

# chroma_client = chromadb.Ephem =eralClient()  # 创建一个内存对象
chroma_client = chromadb.PersistentClient("./chroma_db")  # 创建一个本地存储的对象
chroma_collection = chroma_client.get_or_create_collection("quickstart")

# 设置ChromaVectorStore并加载数据
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
# 创建一个存储容器
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 创建向量索引
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

print(chroma_collection.count())
# 创建检索器
query_retriever = index.as_retriever()
response = query_retriever.retrieve('萧炎的妹妹是谁？')
print(response)

