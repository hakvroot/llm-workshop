# Exercise 1: Embeddings

In this exercise we will start creating embeddings using OpenAI's embedding API. Feel free to use the already imported libraries `openai`, `numpy`, `seaborn`, `sklearn`, or `matplotlib`.

## Part 0: Set up your Environment
Note: If Hermit is already active, use `deactive-hermit` to drop the active Hermit context. 

1. Use `. bin/activate-hermit` in this folder to activate Hermit.
2. Install the Python dependencies using `pip install -r requirements.txt`
3. Setup your API key: `export OPENAI_API_KEY=<my given key>`
4. Run `python exercise-01.py` to run your script.

## Part 1: Embedding Consistency & Self Similarity
Call the OpenAI API twice to create an embedding for the word "Bike" twice. Are the embedding outputs the same? Use the equality operation to test for this.

## Part 2: Calculating Similarity
Of course calculating similarity is more complex than using equals - we will use the cosine similarity from now on. `numpy` is already installed and imported, calculate the similarity for the vector obtained in Part 1.

## Part 3: How Good are Embeddings?
Create embeddings a matrix for the following words

- "Joy"
- "Dog"
- "Puppy"
- "Cat"
- "Despair"
- "Joy the Dog"

You can use the libraries `seaborn`, `sklearn`, and `matplotlib` to create similarity matrices.

Do the embeddings make sense?

## Part 4: Large Text Similarities (Optional)
Find three news articles, where
- two cover the same subject, but from a different source
- one covers a different subject altogether

Create embeddings and calculate the similarities. Are the results as expected?
