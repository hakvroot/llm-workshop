# Exercise 2: Vector Stores

In this exercise we create a Vector Store using OpenAI's vector store API. There is already a file available for upload in data, which you can query later. 

## Part 0: Set up your Environment
Note: If Hermit is already active, use `deactive-hermit` to drop the active Hermit context. 

1. Use `. bin/activate-hermit` in this folder to activate Hermit.
2. Install the Python dependencies using `pip install -r requirements.txt`
3. Setup your API key: `export OPENAI_API_KEY=<my given key>`
4. Run `python exercise-02-setup.py` to run your vector store creation script.
5. Or, run `python exercise-02-search.py` to run your vector store search script.

## Part 1: Create the Vector Store
Create a new vector store and upload `wijkkrant-zwolle-zuid-2025-06.pdf` to it. Print the id for the vector store for use later on

## Part 2: Query the Vector Store
With the vector store created, try to find details on the `Waterloper`. For all the hits, show the file it exists in, the relevance, and a piece of its contents.
