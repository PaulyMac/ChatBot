import tkinter as tk
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


def main():
    load_dotenv()
    pdf = "ve2np-glcay.pdf"
    pdfgen(pdf)


def pdfgen(pdf):
    if pdf is not None:
        # Read the PDF file and extract text
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split the text into chunks for vectorization and similarity search
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=200,
            length_function=len
        )
        chunkgen = text_splitter.split_text(text)

        # Initialize embeddings and vector database
        embeddings = OpenAIEmbeddings()
        vectordb = FAISS.from_texts(chunkgen, embeddings)

        # Create the GUI
        create_gui(vectordb)


def create_gui(vectordb):
    # Function to handle "Ask" button click event
    def ask_question():
        question = entry.get()
        response = search_question_in_documents(question, vectordb)
        response_text.configure(state='normal')
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, response + "\n")
        response_text.configure(state='disabled')
        ask_another_question()

    # Function to prompt the user to ask another question or close the application
    def ask_another_question():
        question = entry.get()
        if question.lower() == "exit":
            root.destroy()
        else:
            entry.delete(0, tk.END)
            response_text.configure(state='normal')
            response_text.insert(tk.END, "Ask another question or type 'exit' to close the application.")
            response_text.configure(state='disabled')

    # Function to handle Enter key press event
    def on_enter(event):
        ask_question()

    # Create the Tkinter window
    root = tk.Tk()
    root.title("ChatBot")
    root.geometry("600x400")

    # Styling
    root.configure(bg='#F4F4F4')
    label_font = ("Helvetica", 14)
    entry_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")
    response_font = ("Helvetica", 12)

    # Question label and entry field
    question_label = tk.Label(root, text="Enter your question:", font=label_font, bg='#F4F4F4')
    question_label.pack(pady=(30, 10))

    entry = tk.Entry(root, width=50, font=entry_font)
    entry.pack()

    # Bind Enter key press event to ask_question function
    entry.bind("<Return>", on_enter)

    # "Ask" button
    ask_button = tk.Button(root, text="Ask", font=button_font, command=ask_question)
    ask_button.pack(pady=(10, 20))

    # Response label and text area
    response_label = tk.Label(root, text="Response:", font=label_font, bg='#F4F4F4')
    response_label.pack()

    response_text = tk.Text(root, width=50, height=10, font=response_font, state='disabled')
    response_text.pack(pady=(10, 20))

    # Start the Tkinter event loop
    root.mainloop()


def search_question_in_documents(question, vectordb):
    # Perform similarity search in vector database
    docs = vectordb.similarity_search(question)

    # Initialize language model and QA chain
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # Run the QA chain on the input documents and question
    response = chain.run(input_documents=docs, question=question)
    return response


if __name__ == '__main__':
    main()
