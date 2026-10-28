from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

# 初始化分割器
splitter = SentenceSplitter(
    # 长度不是字符串长度 是token长度
    chunk_size=512,  # 分割长度
    # 如果分割完之后小于长度,不会有重叠块
    chunk_overlap=50,  # 重叠长度
)

# 读取文件
documents = SimpleDirectoryReader(input_files=['src/data_file/小说.txt']).load_data()

# 分割文段
nodes = splitter.get_nodes_from_documents(documents)

for node in nodes:
    print(repr(node))
    print(len(node.text))
