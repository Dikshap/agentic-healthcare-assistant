import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_folder = "Agentic Healthcare Assistant for Medical Task Automation/"
texts = []
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        texts.append(load_pdf(os.path.join(pdf_folder, file)))

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.create_documents(texts)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")

def retrieve(query):
    vectorstore = FAISS.load_local("faiss_index", embeddings, 
                                    allow_dangerous_deserialization=True)
    results = vectorstore.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results])

if __name__ == "__main__":
    print(retrieve("chronic kidney disease treatment"))