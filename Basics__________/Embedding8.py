# -----------Embedding -------Similarity search use case
import encodings
import numpy as np 
from llm_config import ollama, MODEL 
import ollama

#Create embedding for a set of words
words = ["king", "orange", "apple", "queen", "throne","fruit", "lion","zebra","goat","man", "woman"]

# response = client.embeddings.create(  <-------------This is for openai
response = ollama.embed(
    model = "nomic-embed-text",                            # openai embeding model - "text-embedding-3-large",
    input = words                                          # For openAI - Use  encoding_format = "float"                       
) 

embeddings = response["embeddings"]
print(f"Embedding dimensions: {len(embeddings[0])}")      # Each word is represented in 768 dimensions 
print(f"Number of embeddings :{len(embeddings)}")         # Total 11 words
"""
                    Embedding Dimension
                         768
              <---------------------->

king       →  [0.12, -0.04, 0.81, ...]    ← 768 numbers
orange     →  [0.31,  0.22, 0.15, ...]    ← 768 numbers
apple      →  [0.28,  0.19, 0.17, ...]    ← 768 numbers
queen      →  [0.11, -0.03, 0.79, ...]    ← 768 numbers
throne     →  [0.09, -0.02, 0.75, ...]    ← 768 numbers
...
woman      →  [0.14,  0.01, 0.72, ...]    ← 768 numbers

↑
11 embeddings
"""
# Function to compute dot product between two vectors
def dot_product(vec1, vec2):
    return np.dot(vec1, vec2)

# Compute similarity matrix (dot products between all pairs)
similarity_matrix = np.zeros((len(words), len(words)))
"""
             king  orange  apple  queen  throne ...
king           0      0      0      0      0
orange         0      0      0      0      0
apple          0      0      0      0      0
queen          0      0      0      0      0
throne         0      0      0      0      0
...
"""
for i in range(len(words)):
    for j in range(len(words)):
        similarity_matrix[i][j] = dot_product(embeddings[i], embeddings[j])
        """
                    king   orange   apple   queen   throne   fruit
        king          1.00    0.12     0.10    0.92    0.88     0.15
        orange        0.12    1.00     0.85    0.10    0.08     0.90
        apple         0.10    0.85     1.00    0.09    0.07     0.88
        queen         0.92    0.10     0.09    1.00    0.87     0.12
        throne        0.88    0.08     0.07    0.87    1.00     0.10
        fruit         0.15    0.90     0.88    0.12    0.10     1.00
        """

#-------Printing------
print("\nSimilarity Matrix (Dot Products):")
print("        "+" ".join(f"{word:<8}" for word in words))
for i, word in enumerate(words):
    row_values = " ".join(
        f"{similarity_matrix[i][j]:.4f}"
        for j in range(len(words))
    )
    print(f"{word:<10}{row_values}")