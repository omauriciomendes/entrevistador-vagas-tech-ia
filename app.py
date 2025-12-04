import streamlit as st


st.set_page_config(
    page_title="Entrevistador de Vagas Tech com IA",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Entrevistador de Vagas Tech")
st.write(
    "Preencha as respostas sobre a vaga de tecnologia. "
    "Ao final, clique em Gerar resumo analítico."
)

with st.form("entrevista_form"):
    titulo = st.text_area(
        "1. Qual é o título da vaga e qual o propósito principal desse cargo?",
        placeholder="Exemplo: Especialista em IA para produtora de música. Vai atuar criando agentes, automações e fluxos inteligentes para o estúdio.",
    )

    senioridade = st.text_area(
        "2. Qual a senioridade esperada e por quê?",
        placeholder="Exemplo: Júnior, para aprender no dia a dia, testar soluções e crescer junto com o time.",
    )

    stack = st.text_area(
        "3. Quais tecnologias, frameworks e práticas são essenciais?",
        placeholder="Exemplo: Engenharia de prompts, agentes de IA, GitHub, Copilot, boas práticas de versionamento.",
    )

    soft_skills = st.text_area(
        "4. Quais comportamentos ou atitudes são mais valorizados?",
        placeholder="Exemplo: Proatividade, curiosidade, resolução de problemas, boa comunicação com o time.",
    )

    gerar = st.form_submit_button("Gerar resumo analítico")


def gerar_resumo(titulo, senioridade, stack, soft_skills):
    partes_vazias = [not titulo.strip(), not senioridade.strip(), not stack.strip(), not soft_skills.strip()]
    if any(partes_vazias):
        return "Preencha todas as respostas antes de gerar o resumo."

    resumo = f"""
### Resumo analítico da vaga

**Título e propósito**

{titulo.strip()}

**Senioridade**

{senioridade.strip()}

**Stack técnica e práticas essenciais**

{stack.strip()}

**Soft skills e comportamentos valorizados**

{soft_skills.strip()}

Este resumo foi gerado a partir das informações fornecidas, com foco em clareza e alinhamento da vaga, sem criar descrição formal de vaga, benefícios ou faixa salarial.
"""
    return resumo


if gerar:
    st.subheader("Resultado")
    resumo = gerar_resumo(titulo, senioridade, stack, soft_skills)
    st.markdown(resumo)
