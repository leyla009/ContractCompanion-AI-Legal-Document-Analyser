import os
from google import genai
from dotenv import load_dotenv

# Load secret key assets from the environmental file
load_dotenv()

def analyze_legal_document(document_text):
    """Sends document string data to the modern GenAI Client with structured prompts."""
    # The modern client automatically looks for the GEMINI_API_KEY environment variable.
    # Since we set GOOGLE_API_KEY in your file, we pass it in explicitly to be safe:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    prompt = f"""
    You are an expert legal assistant. Analyze the following legal document text and provide a structured review:
    
    1. **Executive Summary**: A brief overview of what this agreement is.
    2. **Key Entities**: Extract names of parties, critical dates, and governing jurisdiction.
    3. **Risk Analysis**: Identify and flag any highly sensitive, ambiguous, or risky clauses.
    
    Document Text:
    {document_text}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
