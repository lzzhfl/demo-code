from llama_index.core.schema import TextNode, NodeRelationship, RelatedNodeInfo

def link_bidirectional(a: TextNode, b: TextNode, a_note: str, b_note: str):
    a.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
        node_id=b.node_id,  # 关联的目标节点ID（b的唯一标识）
        metadata={"desc": a_note}  # 关系的描述元数据，方便后续追溯
    )
    b.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
        node_id=a.node_id,  # 关联的目标节点ID（a的唯一标识）
        metadata={"desc": b_note}  # 关系的描述元数据
    )

node1 = TextNode(text="deepseek")  # 节点1：文本内容"deepseek"
node2 = TextNode(text="chatgpt")   # 节点2：文本内容"chatgpt"

link_bidirectional(node1, node2, a_note="这是节点2", b_note="这是节点1")

print(repr(node1))
print(repr(node2))
