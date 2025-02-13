import random

temas = {
    "natureza": {
        "substantivos": ["mar", "vento", "sol", "lua", "floresta", "rio", "montanha"],
        "verbos": ["canta", "dansa", "chora", "sussurra", "brilha", "foge", "espera"],
        "adjetivos": ["doce", "amargo", "suave", "eterno", "fugaz", "quieto", "imenso"],
        "adverbios": ["suavemente", "lentamente", "intensamente", "silenciosamente", "eternamente"]
    },
    "amor": {
        "substantivos": ["amor", "coração", "beijo", "abraço", "carinho", "paixão", "sentimento"],
        "verbos": ["ama", "beija", "abraça", "acaricia", "sonha", "deseja", "quer"],
        "adjetivos": ["doce", "amargo", "suave", "eterno", "fugaz", "quieto", "imenso"],
        "adverbios": ["suavemente", "lentamente", "intensamente", "silenciosamente", "eternamente"]
    },
    "tecnologia": {
        "substantivos": ["computador", "celular", "internet", "tecnologia", "inovação", "software", "hardware"],
        "verbos": ["programa", "codifica", "inova", "conecta", "compartilha", "baixa", "acessa"],
        "adjetivos": ["digital", "virtual", "rápido", "lento", "inovador", "antigo", "moderno"],
        "adverbios": ["rapidamente", "lentamente", "intensamente", "silenciosamente", "eternamente"]
    }
}

estruturas = [
    "O {substantivo} {verbo} {adverbio} no {substantivo}.",
    "{adjetivo} como um {substantivo}, o {substantivo} {verbo}.",
    "No {substantivo}, o {substantivo} {verbo} {adverbio}.",
    "Quando o {substantivo} {verbo}, o {substantivo} {verbo} {adverbio}.",
    "Sob o {substantivo}, {adjetivo} e {adjetivo}, o {substantivo} {verbo}.",
    "Entre {substantivo} e {substantivo}, o {substantivo} {verbo} {adverbio}.",
]

def escolher_tema():
    print("Escolha um tema para o poema:")
    for i, tema in enumerate(temas.keys()):
        print(f"{i + 1}. {tema.capitalize()}")
    while True:
        try:
            escolha = int(input("Digite o número do tema: ")) - 1
            if 0 <= escolha < len(temas):
                return list(temas.keys())[escolha]
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def gerar_verso(tema):
    estrutura = random.choice(estruturas)
    palavras = temas[tema]
    verso = estrutura.format(
        substantivo=random.choice(palavras["substantivos"]),
        verbo=random.choice(palavras["verbos"]),
        adjetivo=random.choice(palavras["adjetivos"]),
        adverbio=random.choice(palavras["adverbios"])
    )
    return verso.capitalize()

def gerar_poema(tema, num_estrofes=3, versos_por_estrofe=4):
    poema = []
    for _ in range(num_estrofes):
        estrofe = []
        for _ in range(versos_por_estrofe):
            estrofe.append(gerar_verso(tema))
        poema.append("\n".join(estrofe))
    return "\n\n".join(poema)

def salvar_poema(poema):
    with open("poema_gerado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(poema)
    print("Poema salvo em 'poema_gerado.txt'.")

def main():
    print("Bem-vindo ao gerador de poemas criativos!")
    tema = escolher_tema()
    num_estrofes = int(input("Quantas estrofes você quer? "))
    versos_por_estrofe = int(input("Quantos versos por estrofe? "))

    poema = gerar_poema(tema, num_estrofes, versos_por_estrofe)
    print("\nAqui está o seu poema:\n")
    print(poema)

    if input("\nDeseja salvar o poema em um arquivo? (s/n): ").lower() == "s":
        salvar_poema(poema)

if __name__ == "__main__":
    main()