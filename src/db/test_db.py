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
# Get every single chunk stored in the database as a dictionary
all_docs = vdb._collection.get()

# all_docs['documents'] is a list of all chunk texts
# enumerate gives us both the index number (i) and the chunk text (doc)
for i, doc in enumerate(all_docs['documents']):
    
    # .lower() converts to lowercase so "Shakes" and "shakes" both match
    if 'shakes' in doc.lower():
        
        # f string lets us put the variable i directly into the string
        print(f"FOUND IN CHUNK {i}:")
        
        # Print the full chunk text
        print(doc)
        print("---")