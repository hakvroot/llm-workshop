import openai
import os
import numpy as np

# Create a client using your OpenAI API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # or use api_key="your-key"

# Define the input string
text = "ChatGPT is helpful for many tasks."

# Get the embedding
response = client.embeddings.create(
    model="text-embedding-3-small",  # or "text-embedding-3-large"
    input=text
)

# Extract the embedding vector
embedding = response.data[0].embedding

print(f"Embedding for input:\n{text}\n")
print(f"Vector (length {len(embedding)}):\n{embedding}")

np

# Inputs
text1 = "ChatGPT helps with coding."
text2 = "ChatGPT assists in writing code."

# Get embeddings
embedding1 = client.embeddings.create(model="text-embedding-3-small", input=text1).data[0].embedding
embedding2 = client.embeddings.create(model="text-embedding-3-small", input=text2).data[0].embedding

# Convert to NumPy arrays
vec1 = np.array(embedding1)
vec2 = np.array(embedding2)

# Compute cosine similarity
cosine_similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
cosine_distance = 1 - cosine_similarity
