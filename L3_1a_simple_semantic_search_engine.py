
# Semantic Search - Build a simple document search engine where users can input a query and retrive relevant documents
documents = [
    "Apples and bananas are fruits.",
    "Dogs and cats are friendly animals.",
    "Cars need fuel to run.",
    "Python is a popular programming language.",
    "I love to work in Infosys as a software engineer",
    "Tell me about the industry verticals in Infosys",
    "TCS frontline growth is flat for this quarter."
]

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('all-MiniLM-L6-v2')

doc_embeddings = model.encode(documents) 
print("Doc embeddings.......")
        # [
        #     [0.1, 0.2, 0.3],
        #     [0.4, 0.5, 0.6],
        #     [0.7, 0.8, 0.9]
        # ]

query="What do you think of Indian IT industry"
print("Query embedding....")
query_embedding = model.encode([query])
        # [0.1, 0.2, 0.3]

from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
print(similarities)

zipped_doc_list=list(zip(documents,similarities))

def key_check(x):
    return x[1]

sorted_doc_list=sorted(zipped_doc_list,key=key_check,reverse=True)
# [(tex,value),()]
print('Printing the text based on high value of similarity')
for doc,value in sorted_doc_list:
    print(f" Similarity value:{value}, Doc: {doc}")

# Valeue ranges from 0 to 1, 1 being the most similar

# Printing the text based on high value of similarity
#  Similarity value:0.41215869784355164, Text: Tell me about the industry verticals in Infosys
#  Similarity value:0.35186922550201416, Text: I love to work in Infosys as a software engineer
#  Similarity value:0.25516384840011597, Text: TCS frontline growth is flat for this quarter.
#  Similarity value:0.2004772275686264, Text: Python is a popular programming language.
#  Similarity value:0.018029984086751938, Text: Apples and bananas are fruits.
#  Similarity value:-0.0012345798313617706, Text: Cars need fuel to run.
#  Similarity value:-0.03707125037908554, Text: Dogs and cats are friendly animals.