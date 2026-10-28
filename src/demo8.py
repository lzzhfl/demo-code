from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader

# 加载文件
documents = SimpleDirectoryReader(input_files=['src/data_file/公司规章制度.txt']).load_data()
# 进行切片
parser = SentenceSplitter()

# 将文档解析成节点
nodes = parser.get_nodes_from_documents(documents)
print(repr(nodes[1]))
