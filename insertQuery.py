from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = ChatGroq(model="qwen/qwen3.8-27b", temperature=0)

prompt = ChatPromptTemplate.from_template("""
you are a test data geneartor. genearte {count}  rowa of data for this table as insert queries

 CREATE TABLE users (id INT PRIMARY KEY , name VARCHAR(50) NOT NULL, email VARCHAR (100) UNIQUE, age INT Check(age>=18) , city VARCHAR(30));
RULE: unique ids and and emails, realistics indian names and cities, include 1 row that violates a constraint (age below18)

Return ONLY a json list No extra text """)
chain = prompt | llm | JsonOutputParser()

users  = chain.invoke({"count":5})

for user in users:
    print(user)
