import streamlit as st
import os
from document_processor import extract_text
from ai_engine import analyze_legal_document

st.set_page_config(page_title="ContractCompanion - AI Legal Document Analyzer", layout="centered")
st.title("⚖️ ContractCompanion")
st.write("Your virtual assistant to analyze legal contracts, extract entities, and identify risks.")

# File Uploader Widget
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.info("Processing file and extracting content...")
    
    # Save uploaded file temporarily to pass to our processors
    file_type = uploaded_file.name.split(".")[-1].lower()
    temp_filename = f"temp_doc.{file_type}"
    
    with open(temp_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    try:
        # Step 1: Run through our Document Processor
        extracted_text = extract_text(temp_filename, file_type)
        
        if not extracted_text.strip():
            st.error("Could not extract readable text from this file.")
        else:
            st.success("Text extraction complete! Running AI analysis...")
            
            # Step 2: Run through our AI Engine
            analysis_result = analyze_legal_document(extracted_text)
            
            # Step 3: Render to Screen
            st.markdown("### 📋 AI Analysis Report")
            st.write(analysis_result)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
        
    finally:
        # Clean up local temporary file safely
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

