# GenAI Software Wrapper🦜️🔗 

## Features
- **`Stateless Interaction:`**: Operates without maintaining conversation history, ideal for handling independent queries.
- **`LangChain Integration`**: Uses LangChain for prompt management and chaining LLM interactions.
- **`Google Gemini`**: Interfaces with Google Gemini for generating responses based on user queries.
- **`Streamlit Frontend`**:Provides an interactive web interface for users to input questions and receive responses.

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
In the root directory of your project, create a file named .env and add your API keys:
```bash
GOOGLE_API_KEY=your_google_api_key

```

### Open-source libraries
- **`google-generativeai`**:  Interfaces with Google's Gemini Generative AI model to generate responses based on prompts. This library allows interaction with Google’s generative AI services.
- **`langchain-community`**: Third party integrations.
  - Some integrations have been further split into **partner packages** that only rely on **`langchain-core`**. Examples include **`langchain_openai`** and **`langchain_anthropic`**.
- **`langchain`**: Chains, agents, and retrieval strategies that make up an application's cognitive architecture.
- **`streamlit`**:Provides an interactive web interface for Python scripts. It's used to create the frontend of your application where users can input questions and view responses.

  ##  What is LangChain?
LangChain is a library designed to simplify the development of applications that leverage large language models (LLMs). It provides a framework for integrating LLMs with various tools and services, facilitating complex interactions, and enabling more sophisticated use cases in natural language processing

##  Usage
Run the Streamlit application to start the web interface:
```bash
streamlit run app.py

```
Interact with the Application
- Open your web browser and go to the one url which is created.
- Enter your question in the input field and click "Ask the question."
- The application will display the response in JSON format.

## 📖 API Documentation
Check this [link](https://documenter.getpostman.com/view/38302474/2sAXqndjDb) for full API documentation
- Getting Started
- API Endpoints
- Request and Response Structure
- Error Handling
- Deployment
- Conclusion
  


