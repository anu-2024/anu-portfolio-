import streamlit as st

from components.ui import section_header
from utils.data import load_faq
from utils.text import answer_question, escape, suggested_questions

WELCOME = (
    "Ask me about Anu's projects, skills, experience, education, certifications, "
    "GitHub activity or contact details. I answer from the verified information on this page."
)


def _initial_messages() -> list[dict[str, str]]:
    return [{"role": "assistant", "content": WELCOME}]


def _ask(question: str) -> None:
    faq = load_faq()
    answer, _ = answer_question(question, faq)
    messages = st.session_state.faq_messages
    messages.append({"role": "user", "content": question})
    messages.append({"role": "assistant", "content": answer})


def render_faq() -> None:
    if "faq_messages" not in st.session_state:
        st.session_state.faq_messages = _initial_messages()

    faq = load_faq()
    suggestions = suggested_questions(faq, limit=6)

    section_header(
        "faq",
        "10",
        "Portfolio assistant",
        "Ask about the work.",
        "A lightweight, rule-based FAQ assistant. It runs locally and does not send questions to an external AI service.",
    )

    left, right = st.columns([0.34, 0.66], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="panel faq-side">
              <span class="eyebrow">Quick answers</span>
              <h3>Start with a question.</h3>
              <p>Choose a suggested question or type your own below. Answers are drawn from the projects, experience, education and skills on this page.</p>
              <div class="faq-note">No external AI service is used. If a question is outside the portfolio, the assistant will say so and point you to the relevant section.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for item in suggestions:
            st.button(
                item["question"],
                key=f"faq_suggest_{item['id']}",
                on_click=_ask,
                args=(item["question"],),
                use_container_width=True,
            )

        if st.button("Clear conversation", key="faq_clear", use_container_width=True):
            st.session_state.faq_messages = _initial_messages()
            st.rerun()

        st.caption("Rule-based assistant · answers from local JSON data")

    with right:
        for message in st.session_state.faq_messages:
            with st.chat_message(message["role"]):
                st.markdown(escape(message["content"]))

        with st.form("faq_form", clear_on_submit=True):
            question = st.text_input(
                "Your question",
                placeholder="e.g. Which projects use Generative AI?",
                label_visibility="collapsed",
            )
            submitted = st.form_submit_button("Ask the portfolio assistant", use_container_width=True)

        if submitted and question.strip():
            _ask(question.strip())
            st.rerun()
