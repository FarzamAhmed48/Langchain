from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A Simple API Server"
)

# Load LLMs
openai_llm = ChatOpenAI(model="gpt-3.5-turbo")
ollama_llm = OllamaLLM(model="gemma3:1b")

# Define prompts
prompt_openai = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt_ollama = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

# Add LangChain routes
add_routes(app, openai_llm, path="/openai")  # Just LLM
add_routes(app, prompt_openai | openai_llm, path="/essay")  # Prompt + OpenAI
add_routes(app, prompt_ollama | ollama_llm, path="/poem")  # Prompt + Ollama

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
