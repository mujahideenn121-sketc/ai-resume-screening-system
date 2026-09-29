import streamlit as st
from resume_parser import extract_text_from_pdf
from matcher import calculate_match
from skills import extract_skills

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening System")
st.caption("Python • NLP • TF-IDF • Streamlit")

st.write(
    "Upload a resume and enter a job description to estimate how closely "
    "the resume matches the role."
)

left, right = st.columns(2)

with left:
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with right:
    job_description = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Example: Looking for a Python developer with SQL, Git, REST API and machine learning experience..."
    )

if st.button("Analyze Resume", type="primary"):
    if not resume_file:
        st.warning("Please upload a PDF resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error("Could not extract readable text from this PDF.")
            st.stop()

        score = calculate_match(resume_text, job_description)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        matched = sorted(set(resume_skills) & set(job_skills))
        missing = sorted(set(job_skills) - set(resume_skills))

    st.divider()

    c1, c2, c3 = st.columns(3)
    c1.metric("Match Score", f"{score:.1f}%")
    c2.metric("Matched Skills", len(matched))
    c3.metric("Missing Skills", len(missing))

    st.subheader("📊 Candidate Analysis")

    if score >= 75:
        st.success("Strong alignment with the entered job description.")
    elif score >= 50:
        st.info("Moderate alignment. Some relevant skills are present.")
    else:
        st.warning("Lower alignment. More role-relevant skills may be needed.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Matched Skills")
        if matched:
            for skill in matched:
                st.write(f"• {skill}")
        else:
            st.write("No matching skills detected.")

    with col2:
        st.markdown("### ⚠️ Potentially Missing Skills")
        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.write("No missing skills detected from the built-in skill list.")

    with st.expander("View extracted resume text"):
        st.text(resume_text[:12000])

st.divider()
st.caption("Note: This is an educational screening aid, not a hiring decision system. Results depend on the resume text, job description and built-in skill vocabulary.")
