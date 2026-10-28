from llama_index.core.node_parser import HTMLNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

# 读取文件 FlatReader：从文件中提取原始文本
html_docs = FlatReader().load_data(Path("src/data_file/index.html"))

# 使用 HTMLNodeParser，指定根据哪些标签创建节点
# 需要安装 pip install beautifulsoup4
parser = HTMLNodeParser(tags=["p", "h1", "li"])  # 只提取 p, h1, li 标签的内容作为节点
nodes = parser.get_nodes_from_documents(html_docs)
print(repr(nodes[1]))