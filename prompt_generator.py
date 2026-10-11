from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template="""You are an insightful and engaging literary critic. 

Write a book review based on the following specifications:
- Book Title: {book_title}
- Review Style/Tone: {review_style} 
- Review Length: {review_length} 
Guidelines:
1. Capture the core themes and impact of the book while strictly adopting the requested review style.
2. Adhere strictly to the requested length constraints.
3. Avoid spoilers unless explicitly requested.
4. Keep the language a bit simple

""",
input_variables=["book_title","review_style","review_length"]
)

#this will make a json format of the template and now the prompt can be used accross multiple files
template.save("template1.json")