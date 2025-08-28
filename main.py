from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2:1b")

template = """
You are an Book expert and excellent book recommender and excel in providing book suggestion based on the people's need, preferences, mood, the story they are looking for, etc.
Please return 3 book suggestions.

Here are some relevant descriptions of the some books: {description}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Describe the type of book you want to read today (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    description = retriever.invoke(question)
    result = chain.invoke({"reviews": description, "question": question})
    print(result)