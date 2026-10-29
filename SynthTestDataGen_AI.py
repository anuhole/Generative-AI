from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = ChatGroq(model="qwen/qwen3.8-27b", temperature=0)

prompt = ChatPromptTemplate.from_template("""
you are a test data geneartor. genearte {count} realistic user records for an Indian e-commerce app.
Rules:
-field name, email, phone,city,age
-email must match the perons name
-Phone must be a 10-digit indian mobile
-Include 1 invcalid records(e.g bad email or age below 10) and
add a field "is_valid: false for it; use true for the others

Return ONLY a json list No extra text """)
chain = prompt | llm | JsonOutputParser()

users  = chain.invoke({"count":5})

for user in users:
    print(user)
