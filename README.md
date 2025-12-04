# Entrevistador de Vagas Tech com IA

Este projeto apresenta um entrevistador técnico estruturado para vagas de tecnologia. Ele conduz a entrevista com perguntas uma por vez e, ao final, gera um resumo analítico baseado nas respostas fornecidas pelo usuário. O objetivo é facilitar a criação de descrições de vagas, alinhamentos internos e processos de recrutamento usando lógica simples ou integrado com ferramentas de IA.

## Objetivo do Projeto

Criar uma ferramenta simples e reutilizável que ajuda pessoas de RH, Tech Leads e criadores de conteúdo sobre carreira a conduzirem entrevistas estruturadas sobre vagas de tecnologia. O entrevistador segue um fluxo claro para coletar informações sobre título, propósito da vaga, senioridade, stack técnica e soft skills, gerando um resumo ao final.

## Funcionalidades

* Perguntas uma por vez
* Fluxo estruturado cobrindo quatro áreas
  Título e propósito
  Senioridade
  Stack e práticas essenciais
  Soft skills
* Geração de resumo analítico após confirmação do usuário
* Arquivo de prompt reutilizável para IA
* Script em Python executável no terminal

## Estrutura do Projeto

```
entrevistador-vagas-tech-ia/
  README.md
  src/
    interviewer.py
  prompts/
    entrevistador_ia_tech.md
  examples/
    exemplo_respostas_e_resumo.md
  .gitignore
  LICENSE
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

## Conteúdo do Prompt

O arquivo `prompts/entrevistador_ia_tech.md` contém toda a lógica de comportamento caso você queira usar o entrevistador em uma IA. O prompt segue regras específicas como perguntar uma coisa por vez, nunca criar job description e só gerar o resumo com confirmação.

## Exemplo de Uso

O arquivo `examples/exemplo_respostas_e_resumo.md` mostra uma sessão completa incluindo perguntas, respostas e o resumo gerado.

## Melhorias Futuras

* Criar interface web simples usando Streamlit ou Gradio
* Adicionar suporte para salvar as respostas em JSON
* Integrar com API de IA para gerar resumos mais ricos
* Criar múltiplos modelos de entrevistas
* Adicionar suporte a diferentes idiomas

## Licença

Este projeto pode ser usado livremente de acordo com a licença escolhida pelo autor.

---


