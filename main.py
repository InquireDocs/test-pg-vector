from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.pgvector import PGVector


############################
# Load environment variables
load_dotenv()

################
# Load documents
loader = PyPDFLoader("https://docs.aws.amazon.com/pdfs/wellarchitected/latest/devops-guidance/devops-guidance.pdf")
docs = loader.load_and_split()

############################
# Load documents in PGVector

CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("POSTGRES_DRIVER", "psycopg2"),
    host=os.environ.get("POSTGRES_HOST", "localhost"),
    port=int(os.environ.get("POSTGRES_PORT", "5432")),
    database=os.environ.get("POSTGRES_DB", "test"),
    user=os.environ.get("POSTGRES_USER", "example"),
    password=os.environ.get("POSTGRES_PASSWORD", "example"),
)

COLLECTION_NAME = "devops"

db = PGVector.from_documents(
    embedding=OpenAIEmbeddings(),
    documents=docs,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
)

#######
# Query
query = "What is Continuous Integration?"

print("#" * 80)
print("#" * 80)
print("# Similarity Search with Euclidean Distance (Default)")
print("#" * 80)
print("#" * 80)
docs_with_score = db.similarity_search_with_score(query)
for doc, score in docs_with_score:
    print("-" * 80)
    print("Score: ", score)
    print(doc.page_content)
    print("-" * 80)

print("#" * 80)
print("#" * 80)
print("# Maximal Marginal Relevance Search (MMR)")
print("#" * 80)
print("#" * 80)
docs_with_score = db.max_marginal_relevance_search_with_score(query)
for doc, score in docs_with_score:
    print("-" * 80)
    print("Score: ", score)
    print(doc.page_content)
    print("-" * 80)
