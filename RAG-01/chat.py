from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_model
)

# Take User Query
query = input("> ")

# Vector Similarity Search [query] in DB
search_results = vector_db.similarity_search(
    query=query
)

context = "\n\n\n".join(
    [f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
    You are a helpfull AI Assistant who asnweres user query based on the available context
    retrieved from a PDF file along with page_contents and page number.

    You should only ans the user based on the following context and navigate the user
    to open the right page number to know more.

    Context:
    {context}
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    messages.append({"role": "user", "content": query})
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )
    messages.append(
        {"role": "assistant", "content": response.choices[0].message.content})
    # parsed_response = json.loads(response.choices[0].message.content)
    print(f"🤖: {response.choices[0].message.content}")
    query = input("> ")
    if query.lower() in ["exit", "quit", "stop"]:
        break
