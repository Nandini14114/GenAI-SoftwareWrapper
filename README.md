# GenAI Software Wrapper🦜️🔗 

## Quick Installations

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```
Create a requirements.txt file with the following content:
```bash
flask
langchain
huggingface-hub
python-dotenv

```
Install the dependencies:
```bash
pip install -r requirements.txt

```
##  What is LangChain?
LangChain is a library designed to simplify the development of applications that leverage large language models (LLMs). It provides a framework for integrating LLMs with various tools and services, facilitating complex interactions, and enabling more sophisticated use cases in natural language processing

### Open-source libraries
- **`google-generativeai`**:  Interfaces with Google's Gemini Generative AI model to generate responses based on prompts. This library allows interaction with Google’s generative AI services.
- **`langchain-community`**: Third party integrations.
  - Some integrations have been further split into **partner packages** that only rely on **`langchain-core`**. Examples include **`langchain_openai`** and **`langchain_anthropic`**.
- **`langchain`**: Chains, agents, and retrieval strategies that make up an application's cognitive architecture.
- **`streamlit`**:Provides an interactive web interface for Python scripts. It's used to create the frontend of your application where users can input questions and view responses.
