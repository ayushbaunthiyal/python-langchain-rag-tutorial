from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o-mini")

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_paths=["https://www.educosys.com/course/genai"])

docs = loader.load()
print(docs)

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
splits = text_splitter.split_documents(docs)
# print(splits[0])
# print(splits[1])
# print(splits[2])
print(len(splits))

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# assuming `splits` is your list of documents
# vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# # Optional: check contents of the vectorstore
# print(vectorstore._collection.count())
# print(vectorstore._collection.get())
