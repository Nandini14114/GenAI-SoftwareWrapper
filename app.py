from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

# Load environment variables
load_dotenv()

# Configure Gemini LLM API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a function to interact with the Gemini API
def get_gemini_response(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt, stream=True)
    answer = ""
    for chunk in response:
        answer += chunk.text
    return answer

# Define a LangChain-compatible prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Question: {question}\nAnswer:"
)

# Define a LangChain LLMChain
class SimpleLLMChain:
    def __init__(self):
        self.prompt_template = prompt_template

    def run(self, inputs):
        prompt = self.prompt_template.format(question=inputs['question'])
        answer = get_gemini_response(prompt)
        return {
            "question": inputs['question'],
            "answer": answer
        }

# Create an instance of the simple LLMChain
llm_chain = SimpleLLMChain()

# Streamlit app initialization
st.set_page_config(page_title="Q&A Demo")

st.header("Software Wrapper")

# Input from the user
input = st.text_input("Input your question:", key="input")
submit = st.button("Ask the question")

if submit and input:
    # Get response from the LLMChain
    response = llm_chain.run({"question": input})

    # Convert the response to JSON format
    response_json = json.dumps(response, indent=2)

    st.subheader("The Response in JSON Format:")
    st.json(response_json)
