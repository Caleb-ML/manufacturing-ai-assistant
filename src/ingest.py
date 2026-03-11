# Importing all frameworks and packages to handle the ingestion pipeline from Langchain
from langchain_community.document_loaders import PyPDFLoader

from langchain_core.documents import Document # FOR THE NEW PDFPLUMBER FUNCTION
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import pdfplumber
import os
# Defining a function to load the manuals from folder (data/manuals)
# Storing it into a Loader variable as an intermediate step makes debugging easier - using Langchain

# def load_docs(data_dir: str):
#     docs = []
#     for file in os.listdir(data_dir):
#         if file.endswith(".pdf"): #checking if its a pdf to start loading
#             loader = PyPDFLoader(os.path.join(data_dir, file))
#             docs.extend(loader.load())
#     return docs  

def load_docs(data_dir:str):
    docs = []
    for file in os.listdir(data_dir):
        if file.endswith(".pdf"):
            filepath = os.path.join(data_dir, file) # saves filepath properly , uses join function
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages: # loop thru pdf and extract the text page by page 
                    text = page.extract_text()
                    if text: # ensures text varible isnt empty to avoid storing empty chunks 
                         
                        docs.append(Document(
                            page_content= text,
                            metadata={"source": filepath}
                        ))

    return docs


# Chunking Function which returns the chunked list in chunks                 
def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)

# Creating vector database from chunksand using mistral as the embedder and storing it in Chroma
def create_vdb(chunks):
    embeddings = OllamaEmbeddings(model="mistral")
    vdb = Chroma.from_documents(
        documents = chunks,
        embedding= embeddings,
        persist_directory = "data/chroma_db"
    )
    return vdb
# This IF statement is being run becuase the file is being used directly then execute the pipeline
if __name__ == "__main__":

    print("Loading Documents...")
    docs = load_docs("data/manuals")
    print(f"{len(docs)} pages loaded")
    
    print("Chunking Documents...")
    chunks = chunk_docs(docs)
    print(f"{len(chunks)} chunks created")

    print("Creating Vector Database...")
    create_vdb(chunks)
    print(f"Vector DB saved! ")

