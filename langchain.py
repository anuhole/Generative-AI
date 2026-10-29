from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="qwen/qwen3.8-27b", temperature=0.9)

prompt = ChatPromptTemplate.from_template("""
You are a senior QA engineer. Generate test cases for the following feature:
{feature}

write selenium test cases in java for above feature
""")

chain = prompt | llm | StrOutputParser()

feature = "Login page with username and password. Password must be 8-16 characters."
result = chain.invoke({"feature": feature})
print(result)