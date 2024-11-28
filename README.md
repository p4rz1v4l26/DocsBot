# Conversational-Chatbot

## **Overview**



The Conversational Chatbot allows users to upload PDF documents and interact with them through meaningful dialogues. It leverages advanced AI techniques to answer questions, provide insights, and offer recommendations based on the uploaded document's content.

---

## **Features**

- Upload and parse PDF documents.
- Extract text and chunk it for efficient processing.
- Answer user queries based on the content of the uploaded document.
- Provide an interactive and intuitive interface via Streamlit.
- Powered by OpenAI APIs and LangChain.

---
## **Technologies Used**

- **Python**  
- **Streamlit**: For creating the user interface.  
- **OpenAI API**: For language model interactions.  
- **PyPDF2**: For parsing PDF documents.  
- **LangChain**: For creating an efficient QA pipeline.  
- **FAISS**: For similarity search and vector storage.

---

## **Setup Instructions**

### **Prerequisites**
Ensure the following are installed:
- Python 3.8 or above
- pip (Python package manager)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/p4rz1v4l26/Conversational-Chatbot.git
```
### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```
### **Step 3: Add OpenAI API Key**
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### **Step 4: Replace Meow.png with your own image**
with the proper location of your image.

### **Step 5: Run the Application**
```bash
python -m streamlit run main.py
```

## **License**

This project is licensed under the [MIT License](https://github.com/p4rz1v4l26/Conversational-Chatbot/blob/master/LICENSE).
