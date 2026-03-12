from llama_index.core import StorageContext, VectorStoreIndex

from rag.embedding import embed_model
from rag.indexer import load_documents, split_documents, vector_store

# 读取文档
documents = load_documents()

print("文档数量:", len(documents))

# 切分文本
nodes = split_documents(documents)

print("chunk数量:", len(nodes))

# 打印第一个chunk
print("示例chunk:")
print(nodes[0].text[:200])

# 3 创建 storage context
storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

print("开始创建索引...")
# 4 构建向量索引
index = VectorStoreIndex(
    nodes,
    storage_context=storage_context,
    embed_model=embed_model,
    show_progress=True
)

print("索引创建成功")