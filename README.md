# Entrevistador de Vagas Tech com IA

Este projeto apresenta um entrevistador técnico estruturado para vagas de tecnologia. Ele conduz a entrevista com perguntas uma por vez e, ao final, organiza as respostas num resumo por tema. O arquivo de prompt leva o mesmo fluxo para uma IA, que escreve o resumo analítico. O objetivo é facilitar alinhamentos internos e processos de recrutamento, com um script simples ou com o prompt usado numa ferramenta de IA.

## Objetivo do Projeto

Criar uma ferramenta simples e reutilizável que ajuda pessoas de RH, Tech Leads e criadores de conteúdo sobre carreira a conduzirem entrevistas estruturadas sobre vagas de tecnologia. O entrevistador segue um fluxo claro para coletar informações sobre título, propósito da vaga, senioridade, stack técnica e soft skills, gerando um resumo ao final.

## Funcionalidades

* Perguntas uma por vez
* Fluxo estruturado cobrindo quatro áreas
  Título e propósito
  Senioridade
  Stack e práticas essenciais
  Soft skills
* Resumo por tema após a confirmação do usuário (o resumo analítico escrito fica com a IA, pelo prompt)
* Arquivo de prompt reutilizável para IA
* Script em Python executável no terminal
* Versão web com Streamlit

## Estrutura do Projeto

```
entrevistador-vagas-tech-ia/
  README.md
  app.py                 versão web (Streamlit)
  requirements.txt
  src/
    interviewer.py       versão de terminal
  prompts/
    entrevistador_ia_tech.md
  examples/
    exemplo_respostas_e_resumo.md
  .gitignore
```

## Como Instalar e Executar

Clone o repositório

```
git clone https://github.com/omauriciomendes/entrevistador-vagas-tech-ia.git
cd entrevistador-vagas-tech-ia
```

Execute o script

```
python src/interviewer.py
```

O terminal iniciará o fluxo de perguntas. No final, você pode confirmar se deseja gerar o resumo.

Para a versão web, instale as dependências e rode o Streamlit

```
pip install -r requirements.txt
streamlit run app.py
```

O navegador abre um formulário com as quatro perguntas e o botão para gerar o resumo analítico.

## Conteúdo do Prompt

O arquivo `prompts/entrevistador_ia_tech.md` contém toda a lógica de comportamento caso você queira usar o entrevistador em uma IA. O prompt segue regras específicas como perguntar uma coisa por vez, nunca criar job description e só gerar o resumo com confirmação.

## Exemplo de Uso

O arquivo `examples/exemplo_respostas_e_resumo.md` mostra uma sessão completa: perguntas, respostas, a saída real do script e um exemplo do resumo que o prompt pede a uma IA.

## Melhorias Futuras

* Adicionar suporte para salvar as respostas em JSON
* Integrar com API de IA para gerar resumos mais ricos
* Criar múltiplos modelos de entrevistas
* Adicionar suporte a diferentes idiomas
