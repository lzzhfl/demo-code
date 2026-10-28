from llama_index.core.prompts.default_prompts import (
    DEFAULT_TEXT_QA_PROMPT,
    DEFAULT_REFINE_PROMPT,
    DEFAULT_SUMMARY_PROMPT,
    DEFAULT_TREE_SUMMARIZE_PROMPT,
)

print("=== 标准问答模板  ===")
print(DEFAULT_TEXT_QA_PROMPT.template)

print("\n=== 迭代优化答案模板 ===")
# 高级检索 refine响应模式用的提示词 把检索到的内容先根据一个检索内容生成回答  在那第二个检索内容和上一次的回答在基础上进行迭代优化
print(DEFAULT_REFINE_PROMPT.template)


print("\n=== 总结模板  ===")
print(DEFAULT_SUMMARY_PROMPT.template)

print("\n=== 树状总结模板  ===")
# 高级检索 tree_summarize响应模式用的提示词
# 把检索到的多个 chunk 调用 LLM 进行总结，逐步从“很多小总结”合并成“一个大总结”，最终只返回 1 个连贯的答案。 适合于 长文本 省上下文。
print(DEFAULT_TREE_SUMMARIZE_PROMPT.template)