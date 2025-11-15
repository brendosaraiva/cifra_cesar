acentos_maiusculos = ["á", "à", "ã", "â", "é", "è", "ê", "í", "ì", "î", "ó", "ò", "õ", "ô", "ú", "ù", "û"]
acentos_minusculos = ["Á", "À", "Ã", "Â", "É", "È", "Ê", "Í", "Ì", "Î", "Ó", "Ò", "Õ", "Ô", "Ú", "Ù", "Û"]
especiais = ["*", "!", "%", '"', "#", "¨", "&", "(", ")", "-", "_", "+", ".", ",", "+", "§", "ª", "{", "}", "?", ";",
             ":", "°", "\\", "/", "|", "-", "'", "¬", "¢", "£", "@"]

alfabeto = {
        1: ["A", "a"],
        2: ["B", "b"],
        3: ["C", "c"],
        4: ["D", "d"],
        5: ["E", "e"],
        6: ["F", "f"],
        7: ["G", "g"],
        8: ["H", "h"],
        9: ["I", "i"],
        10: ["J", "j"],
        11: ["K", "k"],
        12: ["L", "l"],
        13: ["M", "m"],
        14: ["N", "n"],
        15: ["O", "o"],
        16: ["P", "p"],
        17: ["Q", "q"],
        18: ["R", "r"],
        19: ["S", "s"],
        20: ["T", "t"],
        21: ["U", "u"],
        22: ["V", "v"],
        23: ["W", "w"],
        24: ["X", "x"],
        25: ["Y", "y"],
        26: ["Z", "z"]
    }


# Criptografar
def criptografar(carta):
    with open("log/mensagem.txt", mode="w", encoding="utf-8") as arquivo:
        "vl -> Velha letra"
        vl = ''
        separador = ", "
        novas_letras = []

        for palavra in carta:
            for letra in palavra:
                for i, lt in enumerate(alfabeto):
                    if letra == alfabeto[lt][0]:
                        if letra in ["W", "X", "Y", "Z"]:
                            if lt == 23:
                                novas_letras.append(alfabeto[1][0])
                            elif lt == 24:
                                novas_letras.append(alfabeto[2][0])
                            elif lt == 25:
                                novas_letras.append(alfabeto[3][0])
                            elif lt == 26:
                                novas_letras.append(alfabeto[4][0])
                        else:
                            novas_letras.append(alfabeto[lt+4][0])

                    elif letra == alfabeto[lt][1]:
                        if letra in ["w", "x", "y", "z"]:
                            if lt == 23:
                                novas_letras.append(alfabeto[1][1])
                            elif lt == 24:
                                novas_letras.append(alfabeto[2][1])
                            elif lt == 25:
                                novas_letras.append(alfabeto[3][1])
                            elif lt == 26:
                                novas_letras.append(alfabeto[4][1])
                        else:
                            novas_letras.append(alfabeto[lt+4][1])

                    else:
                        vl = letra

                if vl in acentos_maiusculos or vl in acentos_minusculos or vl in especiais:
                    novas_letras.append(vl)
            novas_letras.append(" ")

        frase = separador.join(novas_letras).replace(", ", "")
        arquivo.write(frase)


with open("log/teste.txt", mode="r", encoding="utf-8") as arquivo:
    carta = arquivo.read().split()
    criptografar(carta)
