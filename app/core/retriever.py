from core.vector_store import load_vector_store


def retrieve_context(query, k=3):

    vector_db = load_vector_store()

    results = vector_db.similarity_search(query, k=k)

    context = "\n\n".join([doc.page_content for doc in results])

    return context