from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os


# ====================================
# PATHS
# ====================================

DOCS_PATH = "app/data/docs"

DB_PATH = "app/data/chroma_db"


# ====================================
# EMBEDDING MODEL
# ====================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ====================================
# LOAD DOCUMENTS
# ====================================

def load_documents():

    documents = []

    for file in os.listdir(DOCS_PATH):

        if file.endswith(".txt"):

            loader = TextLoader(
                os.path.join(DOCS_PATH, file),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    return documents


# ====================================
# SPLIT DOCUMENTS
# ====================================

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


# ====================================
# CREATE VECTOR DATABASE
# ====================================

def create_vector_store():

    documents = load_documents()

    chunks = split_documents(documents)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )

    vector_db.persist()

    print("✅ ChromaDB vector database created successfully!")


# ====================================
# LOAD VECTOR DATABASE
# ====================================

def load_vector_store():

    vector_db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )

    return vector_db

