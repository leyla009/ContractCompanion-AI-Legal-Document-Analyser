from document_processor import extract_text
from ai_engine import analyze_legal_document

print("🔄 Step 1: Extracting text from local file...")
text = extract_text("test_contract.txt", "txt")
print("✅ Text successfully extracted!\n")

print("🧠 Step 2: Shipping text to Gemini AI Engine...")
analysis = analyze_legal_document(text)
print("\n📋 --- AI ANALYSIS REPORT ---")
print(analysis)
