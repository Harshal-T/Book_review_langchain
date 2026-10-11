from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline


# This downloads the model to your machine once, then runs entirely locally
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", max_new_tokens=100)
hf_llm = HuggingFacePipeline(pipeline=pipe)

model = ChatHuggingFace(llm=hf_llm)
result = model.invoke("What is the capital of India")
print(result.content)