# Books-Recommendations-using-RAG 📚

This project is a command-line book recommendation system that uses a local Large Language Model (LLM) powered by **Ollama**. It leverages the **Retrieval-Augmented Generation (RAG)** technique to provide contextually relevant book suggestions based on user queries.

The application uses a vector database (**ChromaDB**) to store and retrieve relevant text chunks, which are then fed to the LLM to generate personalized recommendations.

---

## Key Features 🚀
- **Local First**: Runs entirely on your local machine using Ollama, ensuring privacy and no API costs.  
- **RAG Pipeline**: Implements a RAG architecture to ground the LLM's responses in specific data, leading to more accurate and relevant recommendations.  
- **Vector Search**: Uses ChromaDB as a local vector store for efficient similarity searches.  
- **Customizable Data**: Easily adaptable to use your own dataset of book summaries, reviews, or descriptions.  
- **Built with LangChain**: Leverages the LangChain framework to orchestrate the different components (LLM, prompt, retriever).  

---

## How It Works ⚙️

The project is split into two main scripts:

### `vector.py` - The Indexer
- Reads data from a CSV file (`BooksDatasetProcessed.csv`).  
- Uses the `mxbai-embed-large` model via Ollama to create vector embeddings for each entry.  
- Stores these embeddings in a persistent local ChromaDB vector database.  
- This process only needs to be run once to create the database.  

### `main.py` - The Recommender
- Takes a user's request for a book type (e.g., *"a sci-fi book about space exploration"*).  
- Uses the retriever from `vector.py` to find the 5 most semantically similar documents from the ChromaDB.  
- Injects these retrieved documents as context into a prompt template.  
- Sends the enriched prompt to a local LLM (`llama3.2:1b`) to generate **three book recommendations**.  
- The application runs in a loop, allowing for continuous interaction.  

---

## Setup and Installation

### Prerequisites
You must have **Ollama** installed and running on your system.

1. Install Ollama.  
2. Pull the necessary LLM and embedding models:  

```bash
ollama pull llama3.2:1b
ollama pull mxbai-embed-large
```
Installation Steps

1: Download the Dataset:
``` bash
https://drive.google.com/file/d/1ph7gd-MAbqweWz7nHPiOQ7CYJGajCe2u/view?usp=sharing
```
2: Create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3: Install the required dependencies:
```bash
pip install -r requirements.txt
```
4: Prepare your data file:

The script is currently configured to use BooksDatasetProcessed.csv.

Replace it with a dataset of book reviews or summaries.

The CSV file must contain at least the columns: Title, Review, Rating, Date.

Example books.csv structure:
```bash
Title,Review,Rating,Date
"Dune","A sprawling sci-fi epic about politics, religion, and giant sandworms on a desert planet.",5,"1965-08-01"
"Project Hail Mary","An astronaut wakes up with amnesia on a solo mission to save Earth. Witty, scientific, and heartwarming.",5,"2021-05-04"
```
If you use a different filename or column names, update them in vector.py.



### How to Run the Application
1. Create the Vector Database
Run the vector.py script to process your CSV and create the local vector database:

```bash
python vector.py
```
This will create a ./chrome_langchain_db directory in your project folder.

2. Start the Recommender
Now, run the recommender:
```bash
python main.py
```
You can now type your book requests at the prompt!

Type q to quit.

