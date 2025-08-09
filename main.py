import chromadb
import pandas as pd

# create chromaDB client
chroma_client = chromadb.Client()

# create a collection
collection = chroma_client.create_collection(name="my_collection")

# create a dataframe
df = pd.read_csv("poem_data.csv")
df = df.dropna() # drop null values because chromadb expects string non NA
print(df.head())


# Prepare data for ChromaDB
documents = df['Poem'].tolist()                  
metadatas = [{'Genre': Genre} for Genre in df['Genre']]  


# Add documents + metadata to collection
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=[str(i) for i in range(len(documents))]  # optional unique IDs
)

# query the results
results = collection.query(
    query_texts=["Storms are generous."], # Chroma will embed this for you
    n_results=3 # how many results to return
)
print(results)

# print the results in clean way
for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"Document: {doc}")
    print(f"Metadata: {meta}")
    print("-" * 40)