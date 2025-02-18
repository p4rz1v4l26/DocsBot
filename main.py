from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import OpenAI
from langchain_community.callbacks.manager import get_openai_callback

# Load environment variables
load_dotenv()

# Set page configuration as the first Streamlit command
img = Image.open(r"C:\Users\waral\Desktop\Github\Conversational-Chatbot\meow.png")
st.set_page_config(page_title="Conversational Chatbot", page_icon=img)

st.header("DocsBot - Interact with Your Document📄")

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# File uploader
pdf = st.file_uploader("Upload your document", type="pdf")

if pdf is not None:
    # Read the PDF content
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split text into manageable chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Create embeddings and knowledge base
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Conversational chain setup
    llm = OpenAI()
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=knowledge_base.as_retriever()
    )

    st.markdown("### Suggested Questions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("What is this document about?"):
            query = "What is this document about?"
    with col2:
        if st.button("Summarize this document."):
            query = "Summarize this document."
    with col3:
        if st.button("Key takeaways?"):
            query = "What are the key takeaways from this document?"

    # User input for a custom question
    user_query = st.text_input("Ask your question:")
    if user_query:
        query = user_query

    # Run the conversational chain
    if "query" in locals() and query:
        with st.spinner("Thinking..."):
            response = conversational_chain({"question": query, "chat_history": st.session_state.history})
            st.session_state.history.append((query, response["answer"]))
            st.markdown(f"**Response:** {response['answer']}")

        # Show conversation history
        st.markdown("### Conversation History")
        for i, (q, a) in enumerate(st.session_state.history):
            st.write(f"**Q{i+1}:** {q}")
            st.write(f"**A{i+1}:** {a}")

    # Feedback section
    st.markdown("### Feedback")
    feedback = st.radio("Was this response helpful?", ["Yes", "No"], index=0, horizontal=True)
    if feedback == "No":
        st.text_input("Tell us how we can improve:", key="feedback_text")
