from llama_index.core import SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import VectorStoreIndex
from base_llm import llm, embed_model

# 加载文档
documents = SimpleDirectoryReader(input_files=["src/data_file/小说.txt"]).load_data()
# 创建索引
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# 将索引存储在本地
index.storage_context.persist("./vector_store_index")
retriever = index.as_retriever()
print(retriever.retrieve('萧炎父亲是谁'))

# 从本地加载已存储的索引数据
new_storage_context = StorageContext.from_defaults(persist_dir="./vector_store_index")
new_index = load_index_from_storage(new_storage_context, embed_model=embed_model)
print(new_index.as_retriever().retrieve('古河是谁?'))
# 结束