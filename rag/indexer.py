from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


def load_documents():

    documents = SimpleDirectoryReader(
        "data/docs"
    ).load_data()

    return documents

def split_documents(documents):

    splitter = SentenceSplitter(
        chunk_size=512,
        chunk_overlap=50
    )

    nodes = splitter.get_nodes_from_documents(documents)

    return nodes


client = QdrantClient("localhost", port=6333)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="office_docs"
)