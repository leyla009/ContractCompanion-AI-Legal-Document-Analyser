import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load key assets from the secret .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_legal_document(document_text):
    """Sends document string data to the LLM with structured analytical prompts."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    You are an expert legal assistant. Analyze the following legal document text and provide a structured review:
    
    1. **Executive Summary**: A brief overview of what this agreement is.
    2. **Key Entities**: Extract names of parties, critical dates, and governing jurisdiction.
    3. **Risk Analysis**: Identify and flag any highly sensitive, ambiguous, or risky clauses.
    
    Document Text:
    {document_text}
    """
    
    response = model.generate_content(prompt)
    return response.text
