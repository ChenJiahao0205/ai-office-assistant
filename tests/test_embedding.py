from rag.embedding import embed_model

text = "这是一个AI办公助手的测试文本"

vector = embed_model.get_text_embedding(text)

print("向量维度:", len(vector))
print("向量前5个值:", vector[:5])