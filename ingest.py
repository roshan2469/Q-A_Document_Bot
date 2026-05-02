import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_PATH = "data"
DB_PATH = "vectorstore"

def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)
        else:
            continue

        documents.extend(loader.load())

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_documents(documents)

def create_vectorstore(chunks):
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory=DB_PATH
    )

    db.persist()
    print("Vector DB created successfully!")

if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    def create_vectorstore(chunks):
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        db = Chroma.from_documents(
          chunks,
          embedding,
          persist_directory=DB_PATH
        )

        db.persist()
        print("Vector DB created successfully!")

    create_vectorstore(chunks)