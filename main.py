from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

DB_PATH = "vectorstore"

def load_db():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    return db

def ask_question():
    db = load_db()
    llm = Ollama(model="phi")

    while True:
        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        docs = db.similarity_search(query, k=4)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Answer ONLY from the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        print("\nAnswer:")
        print(response)

        print("\nSources:")
        for doc in docs:
            print(doc.metadata)

if __name__ == "__main__":
    ask_question()