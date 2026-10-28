from llama_index.readers.web import FireCrawlWebReader
import os
from dotenv import load_dotenv
load_dotenv()

reader = FireCrawlWebReader(
    api_key=os.getenv("FIRECRAWL_API_KEY"),   # 需要去 https://firecrawl.dev 免费注册获取
    mode="scrape",          # "scrape" 单页 | "crawl" 整站爬取
)
# 加载单个或多个 URL
documents = reader.load_data("https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006,at_1")

print(documents[0].text)