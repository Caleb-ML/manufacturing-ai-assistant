# This script focuses on the RAG process from the question from the user, loading into the Chroma db
# searching for the most relevant chunks using vector similarity, building context with a prompt for the LLM and getting an answer back
# return with citations this whole flow is RAG!

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
# Load the db again and initialse the embeddingModel for the user query
def load_vdb():
    embeddings = OllamaEmbeddings(model="mistral")
    return Chroma(
        persist_directory="data/chroma_db",
        embedding_function= embeddings,
    )
# a function to get the top 3 chunks similar to the users query 
def retrieve_context(query:str,vdb, k:int=5):
    results = vdb.similarity_search(query, k=k)
    return results
   
def build_prompt():
    template = """
You are a manufacturing assistant helping machine operators diagnose faults.
Use ONLY the context provided below to answer the question.
If the answer is not in the context, say "I don't have enough information to answer this safely."
Always cite which document your answer comes from.

Context:
{context}

Question:
{question}

Answer:
"""
    return PromptTemplate(
        input_variables=["context","question"],
        template = template
    )
# the function that puts everything together 
def answer_question(query:str):
    vdb = load_vdb()
    results = retrieve_context(query,vdb)
    # Joining the 3  chunks into one single string separated by blank lines to use as context in the prompt formatting it 

    context = "\n\n".join([doc.page_content for doc in results])

    # Obtaining the source filename from each retrieved chunks metadata for citations otherwise return Unknown if not available ,prevents hallucination
    sources = [doc.metadata.get("source", "Unknown")for doc in results]
# Empty prompt
    prompt = build_prompt()
    # the llm model is the same for the user to talk to essentially
    llm = ChatOllama(model="mistral")
# pipe operator from Langchain, building chains LCEL
    chain = prompt|llm
    # fill in prompt and send to Mistral and get response
    response = chain.invoke({"context": context, "question":query})
# returning dictionary for the UI to display
    return {
        "answer" : response.content,
        "sources" : sources
    }

if __name__ == "__main__":
    query = " machine shakes heavy ?"
    result = answer_question(query)
    print("\n----ANSWER----")
    print(result["answer"])

    print("\n----SOURCES----")
    for inc in result["sources"]:
        print(inc)
