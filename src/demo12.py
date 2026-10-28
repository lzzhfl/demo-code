from llama_index.core.node_parser import JSONNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

# 读取文件 FlatReader：从文件中提取原始文本
json_docs = FlatReader().load_data(Path("src/data_file/request.json"))

# 构建JSON节点解析器
parser = JSONNodeParser()
# 生成节点
nodes = parser.get_nodes_from_documents(json_docs)
print(repr(nodes[0]))
