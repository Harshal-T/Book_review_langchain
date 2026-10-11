from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
st.header("Book reviews here!")
book_title=st.text_input("Enter book name:",)
review_style = st.selectbox( "Select Review Style", ["Beginner-Friendly", "Critic", "Public review overview", "Practical","Casual"] )
review_length = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template=PromptTemplate(
#     template="""You are an insightful and engaging literary critic. 

# Write a book review based on the following specifications:
# - Book Title: {book_title}
# - Review Style/Tone: {review_style} 
# - Review Length: {review_length} 
# Guidelines:
# 1. Capture the core themes and impact of the book while strictly adopting the requested review style.
# 2. Adhere strictly to the requested length constraints.
# 3. Avoid spoilers unless explicitly requested.
# 4. Keep the language a bit simple

# """,
# input_variables=["book_title","review_style","review_length"]
# )


#this is when we have made a json file for prompt template
template=load_prompt("template1.json")

prompt=template.invoke({
    "book_title":book_title,
    "review_style":review_style,
    "review_length":review_length
})
# result=model.invoke("Who is the President of India")
# print(result)

if st.button("Give Review",type="primary"):
    with st.spinner("Writing review..."):
     result=model.invoke(prompt)
     st.markdown(result.content[0]["text"])
