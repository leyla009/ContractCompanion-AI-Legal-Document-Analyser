import streamlit as st
import os
from dotenv import load_dotenv
from document_processor import extract_text
from ai_engine import analyze_legal_document

load_dotenv()

# --- SaaS UI Configuration ---
st.set_page_config(page_title="ContractCompanion - AI Legal Auditor", layout="wide", page_icon="⚖️")

# --- Premium Sidebar Status ---
with st.sidebar:
    st.title("💼 Workspace Control")
    st.markdown("---")
    st.subheader("Account Tier: **Free Tier Plan**")
    
    # SaaS Usage Meter Simulation
    scans_left = 3
    st.progress(scans_left / 5)
    st.caption(f"📊 Usage: {scans_left} out of 5 monthly free scans remaining.")
    
    st.markdown("---")
    st.info("💡 Upgrade to **Premium Enterprise** for unlimited batch contract analysis, custom legal playbooks, and automated NDA redlining.")

# --- Main Dashboard Header ---
st.title("⚖️ ContractCompanion AI")
st.subheader("Enterprise-Grade Legal Document Risk Auditing Micro-SaaS")
st.markdown("---")

# --- Interactive Micro-SaaS Simulation Widget ---
st.write("### 🎛️ Interactive SaaS Sandbox: Liability Calculator")
st.write("Before analyzing a live file, evaluate your contract risk footprint by adjusting standard liability levers:")

# Layout for controls
col1, col2 = st.columns([1, 2])

with col1:
    indemnity_cap = st.slider("Indemnity Limitation ($)", min_value=0, max_value=500000, value=50000, step=10000)
    governing_state = st.selectbox("Governing Jurisdiction", ["California", "Delaware", "New York", "Texas"])
    has_arbitration = st.checkbox("Include Mandatory Arbitration Clause", value=True)

with col2:
    # Mechanical Logic: Calculate an interactive dynamic score based on parameter states
    base_score = 30
    if indemnity_cap < 100000:
        base_score += 40
    if not has_arbitration:
        base_score += 20
        
    st.write("#### Live Contract Liability Assessment")
    if base_score > 60:
        st.error(f"🔴 HIGH RISK SCORE: {base_score}/100")
        st.write(f"**Vulnerability Alert:** An indemnity cap of ${indemnity_cap:,} in {governing_state} without structural limits exposes your organization to severe liability outlays.")
    else:
        st.success(f"🟢 LOW RISK SCORE: {base_score}/100")
        st.write("**Status:** Contractual levers are balanced safely for standard standard operations.")

st.markdown("---")

# --- Live Document Analyzer Section ---
st.write("### 📂 Live Contract Upload & Processing")
uploaded_file = st.file_uploader("Drop your PDF, DOCX, or TXT contract file here for AI extraction...", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if st.button("🚀 Execute Comprehensive AI Risk Audit"):
        with st.spinner("🔄 Parsing document arrays and initializing GenAI compliance audit..."):
            try:
                # Determine file format extension type
                file_extension = uploaded_file.name.split(".")[-1].lower()
                
                # Save uploaded file temporarily to pass to processor
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Extract text layer via processor module
                text = extract_text(uploaded_file.name, file_extension)
                
                # Clean up local temporary file system footprint
                os.remove(uploaded_file.name)
                
                # Invoke modern GenAI engine
                analysis_report = analyze_legal_document(text)
                
                # Display finalized professional output
                st.markdown("---")
                st.success("✅ Analysis Complete!")
                st.write("### 📋 AI Compliance & Risk Audit Report")
                st.markdown(analysis_report)
                
                # SaaS Feature: Export Functionality
                st.markdown("---")
                st.download_button(
                    label="📥 Download Structured Audit Report (.md)",
                    data=analysis_report,
                    file_name=f"Audit_Report_{uploaded_file.name}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"An unexpected process error occurred: {e}")
