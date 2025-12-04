def perguntar(pergunta):
    print()
    return input(pergunta + "\n> ")

def main():
    print("Olá. Vou fazer perguntas sobre a vaga que você está estruturando.")
    
    titulo = perguntar("Para começar, qual é o título da vaga e qual o propósito principal desse cargo?")
    
    senioridade = perguntar("Qual a senioridade esperada e por quê?")
    
    stack = perguntar("Quais tecnologias, frameworks e práticas são essenciais?")
    
    soft_skills = perguntar("Quais comportamentos ou atitudes são mais valorizados?")

    confirmar = perguntar("Quer que eu gere agora o resumo analítico da vaga com base nas suas respostas? (s ou n)")
    
    if confirmar.lower().startswith("s"):
        print("\nResumo analítico da vaga\n")
        print(f"Título e propósito: {titulo}")
        print(f"Senioridade: {senioridade}")
        print(f"Stack essencial: {stack}")
        print(f"Soft skills valorizadas: {soft_skills}")
    else:
        print("\nOk. Você pode rodar o programa novamente quando quiser.")

if __name__ == "__main__":
    main()
