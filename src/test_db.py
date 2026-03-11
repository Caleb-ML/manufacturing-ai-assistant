from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model = "mistral")

vdb = Chroma(embedding_function=embeddings,persist_directory="data/chroma_db")
print(vdb._collection.count())

# Testing with a higher k value to see if injection pdf is being read

results = vdb.similarity_search("machine shakes", k=10)
for result in results:
    print("SOURCE:", result.metadata.get("source"))
    print("TEXT:", result.page_content[:400])
    print("---")
# locating the chunk directly since shakes chunk not coming up with s.s
all_docs = vdb._collection.get()
for i, doc in enumerate(all_docs['documents']):
    if 'shakes' in doc.lower():
        print(f"FOUND IN CHUNK {i}:")
        print(doc)
        print("---")