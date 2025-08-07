
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="CARE-ITS AI Readiness Checklist", layout="centered")
st.title("CARE-ITS AI Readiness Checklist")
st.subheader("Framework Checklist for Nursing Education – Institutions & Developers")
st.markdown("Complete the checklist below to evaluate readiness for AI-enhanced educational technologies in nursing.")

score_map = {"Yes": 1, "Partially": 0.5, "No": 0}
responses = {}
section_scores = {}

def checklist_section(title, questions):
    st.markdown(f"### {title}")
    section_score = 0
    for q in questions:
        response = st.radio(q, ["Yes", "Partially", "No"], key=q)
        responses[q] = response
        section_score += score_map[response]
    section_scores[title] = section_score
    st.markdown("---")

checklist_section("1. Cognitive-First (Start with Knowledge & Reasoning Tasks)", [
    "Have we identified which learning objectives are best suited for AI delivery (vs. human-led)?",
    "Have we ensured AI focuses first on cognitive domain tasks (e.g. recall, reasoning)?",
    "Are more complex domains (e.g. psychomotor, affective) reserved for human interaction?"
])

checklist_section("2. Awareness", [
    "Have we assessed users’ initial understanding of AI (e.g. via survey or workshop)?",
    "Have we addressed misconceptions (e.g. AI = robot)?",
    "Do users understand what AI will and will not do?"
])

checklist_section("3. Retention of Human Touch", [
    "Is there a clear boundary between AI-led and human-led interactions?",
    "Are empathy, communication, and clinical judgement skills taught face-to-face?",
    "Are tutors still part of the process, not replaced?"
])

checklist_section("4. Ethics", [
    "Is the AI system explainable (i.e. does it show how decisions were made)?",
    "Are data privacy and security clearly addressed and explained to users?",
    "Have ethical concerns specific to nursing values been considered?"
])

checklist_section("5. Involvement", [
    "Have nurses and nursing students been involved in co-design or feedback?",
    "Is their input visible in the system’s structure/content?",
    "Do they have a voice in future improvements?"
])

checklist_section("6. Time", [
    "Is there adequate time allocated for onboarding and adaptation?",
    "Is the training optional or mandatory? If mandatory, is it flexible and fair?",
    "Is the AI system introduced in a non-overwhelming way (e.g. with early demos or opt-ins)?"
])

checklist_section("7. System Evaluation", [
    "Has a pilot test been conducted (10–15 users for qualitative insights)?",
    "Is there a plan for continuous feedback and improvement?",
    "Are success metrics defined (e.g. usability, learning outcomes, trust)?"
])

if st.button("✅ Submit and Calculate Score"):
    total_possible = len(responses)
    total_score = sum(score_map[v] for v in responses.values())
    percent = (total_score / total_possible) * 100

    st.success(f"🎯 Overall Score: {percent:.1f}%")
    if percent >= 90:
        st.info("Excellent readiness! You are well-prepared for AI integration.")
    elif percent >= 70:
        st.warning("Moderate readiness. Consider reviewing specific areas.")
    else:
        st.error("Low readiness. Consider strengthening multiple framework areas.")

    st.markdown("### 📊 Section Breakdown:")
    for section, score in section_scores.items():
        max_score = 3
        st.write(f"{section}: {score}/{max_score} ({(score/max_score)*100:.0f}%)")

    st.markdown("### 📈 Visual Summary")
    fig, ax = plt.subplots()
    categories = list(section_scores.keys())
    values = list(section_scores.values())
    colors = ['green' if v == 3 else 'orange' if v == 2 else 'red' for v in values]
    ax.barh(categories, values, color=colors)
    ax.set_xlim(0, 3)
    ax.set_xlabel("Score (0–3)")
    ax.invert_yaxis()
    st.pyplot(fig)
