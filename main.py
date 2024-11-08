from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to your career advisor API!"}

@app.get("/analyze")
def analyze_job():
    # Sample request to OpenAI API (add your logic here)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Analyze job suitability for a candidate.",
        max_tokens=50
    )
    return {"OpenAI response": response.choices[0].text.strip()}