# Exemplo de entrevista completa

Abaixo um exemplo de sessão com o script `interviewer.py`.

## Perguntas e respostas

Pergunta  
Qual é o título da vaga e qual o propósito principal desse cargo?  

Resposta  
Especialista em IA para uma produtora de música. Vai atuar criando agentes, automações e fluxos inteligentes para apoiar a criação musical e a rotina do estúdio.

Pergunta  
Qual a senioridade esperada e por quê?  

Resposta  
Júnior. A ideia é trazer alguém em início de carreira para aprender no dia a dia, testar soluções e crescer junto com o time criativo e técnico.

Pergunta  
Quais tecnologias, frameworks e práticas são essenciais?  

Resposta  
Engenharia de prompts, agentes de IA, GitHub, Copilot e boas práticas de versionamento e colaboração em código.

Pergunta  
Quais comportamentos ou atitudes são mais valorizados?  

Resposta  
Proatividade, curiosidade, vontade de aprender, resolução de problemas e boa comunicação com o time criativo.

## Saída real do script

Depois da confirmação, o `interviewer.py` imprime as respostas organizadas por tema:

```
Resumo analítico da vaga

Título e propósito: Especialista em IA para uma produtora de música. Vai atuar criando agentes, automações e fluxos inteligentes para apoiar a criação musical e a rotina do estúdio.
Senioridade: Júnior. A ideia é trazer alguém em início de carreira para aprender no dia a dia, testar soluções e crescer junto com o time criativo e técnico.
Stack essencial: Engenharia de prompts, agentes de IA, GitHub, Copilot e boas práticas de versionamento e colaboração em código.
Soft skills valorizadas: Proatividade, curiosidade, vontade de aprender, resolução de problemas e boa comunicação com o time criativo.
```

## Resumo analítico no formato do prompt

O script não reescreve as respostas. O texto abaixo é um exemplo do resumo que o prompt em `prompts/entrevistador_ia_tech.md` pede quando é usado numa IA:

Título e propósito  
A vaga é para Especialista em IA em uma produtora de música, com foco em criar agentes, automações e fluxos inteligentes que apoiam a criação musical e a rotina do estúdio.

Senioridade  
O nível júnior foi escolhido porque a empresa busca alguém em início de carreira, com espaço para aprender, experimentar e crescer em conjunto com o time, lidando com tarefas de execução, testes e melhoria contínua.

Stack técnica  
São essenciais conhecimentos em engenharia de prompts, uso de agentes de IA, GitHub, Copilot e boas práticas de versionamento e colaboração, sempre aplicados ao contexto de produção musical e fluxos criativos.

Soft skills  
São valorizadas atitudes como proatividade, curiosidade, capacidade de resolver problemas, disposição para aprender coisas novas e boa comunicação com o time, conectando o universo técnico de IA ao dia a dia musical.
