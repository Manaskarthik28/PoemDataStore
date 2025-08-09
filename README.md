:

📚 Poem Vector Database
A semantic search tool using ChromaDB to store and retrieve poems based on vector embeddings.
Given a poem dataset, it finds the top 3 most similar poems along with their genres.

Features
Store poems with genre metadata in ChromaDB

Query using natural language

Retrieve top N similar poems with semantic search

Tech Stack
Python

ChromaDB

Pandas

Dataset: poem_data.csv (Poem, Genre)

How to Run
Install dependencies:

bash
Copy
Edit
pip install chromadb pandas
Place poem_data.csv in the project folder.

Run:

bash
Copy
Edit
python main.py
