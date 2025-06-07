import openai
import os

# 1. Initialize the OpenAI client with your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Query the vector store
query = "What is the role of embeddings in vector search?"

query_result = client.vector_stores.query(
    vector_store_id=vector_store.id,
    query=query,
    return_metadata=True,
    return_documents=True,
    top_k=3,
)

# 3. Display the results
print("\n🔍 Top relevant results:\n")
for i, result in enumerate(query_result.data, 1):
    print(f"{i}. File ID: {result.document.file_id}")
    print(f"   Relevance Score: {result.score:.4f}")
    print(f"   Snippet: {result.document.text[:200]}...\n")
