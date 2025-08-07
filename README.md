
# CARE-ITS: AI Readiness Checklist for Nursing Education

This is an interactive Streamlit app designed to help **institutions**, **AI developers**, and **educators** evaluate their readiness for implementing AI technologies in nursing education.

The framework builds on grounded theory findings from nursing professionals, distinguishing what should remain **human-led** (e.g., affective/psychomotor skills) and what can be **AI-supported** (e.g., cognitive knowledge tasks).

---

## CARE-ITS Pillars Explained

| Pillar | Description |
|--------|-------------|
| **C – Cognitive-First** | Begin AI implementation by focusing on the **cognitive domain** (knowledge, reasoning). Reserve complex skills like empathy or manual techniques for human-led teaching. This helps build trust without overwhelming users. |
| **A – Awareness** | Assess and improve the **understanding of AI** among users. Many nurses equate AI with robots or surveillance. Clarify that AI can offer personalised feedback, not just automation. |
| **R – Retention of Human Touch** | Maintain **face-to-face teaching** for empathy, communication, and clinical judgement. Clearly define what AI does **not** replace (e.g., mentorship, compassion). |
| **E – Ethics** | Ensure AI systems are **transparent, explainable**, and respect **data privacy**. Institutions should follow ethical policies that align with nursing values. |
| **I – Involvement** | Co-design with nurses and students. Their participation ensures the system meets **real needs** and encourages adoption through ownership. |
| **T – Time** | Give users adequate **time to adapt**. Avoid overwhelming training—use demos, workshops, or opt-ins rather than mandatory rollouts. |
| **S – System Evaluation** | Pilot test with 10–15 users before deployment. Collect ongoing **feedback** and define clear **success metrics** (e.g., trust, usability, outcomes). |

---

## How to Run

### 🔧 Local (Python ≥3.8)

```bash
pip install -r requirements.txt
streamlit run care_its_checklist_app.py
```

### Streamlit Cloud

1. Push this repository to GitHub.
2. Go to https://streamlit.io/cloud
3. Click **“Deploy”** and paste your GitHub repo URL.
4. Done! 

---

## Features

- Scored checklist (Yes / Partially / No)
- Individual scores by CARE-ITS pillar
- Automatic bar chart display
- Feedback based on overall readiness
- Modular code – easy to extend for new frameworks

---

## Who Should Use This?

- **Nursing institutions** preparing for AI integration
- **AI developers** designing educational tools for nurses
- **Policy makers** evaluating readiness and equity of AI systems in healthcare education

---

##  Contact

If you use this tool or adapt it in your work, feel free to [open an issue](https://github.com/yourrepo/issues) or reach out.
