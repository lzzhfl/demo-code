from llama_index.readers.file import PDFReader, DocxReader
from llama_index.core import SimpleDirectoryReader


file_extractor = {
    ".pdf": PDFReader(),   # 处理pdf文件 以页的形式加载成Document
    ".docx": DocxReader(), # 处理docx文件 整个文件是一个Document
}

documents = SimpleDirectoryReader(
    input_dir="./src/data_file",
    required_exts=[".pdf", ".docx", ".md", ".txt"],
    file_extractor=file_extractor,
    recursive=True,
    exclude_empty=True,
).load_data()

for doc in documents:
    print(repr(doc))

