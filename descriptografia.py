from criptografia import alfabeto, acentos_minusculos, acentos_maiusculos, especiais


def descriptografar(carta):
    with open("log/mensagem_descriptografada.txt", mode="w", encoding="utf-8") as arquivo:
        vl = ''
        separador = ", "
        novas_letras = []

        for palavra in carta:
            for letra in palavra:
                for i, lt in enumerate(alfabeto):
                    if letra == alfabeto[lt][0]:
                        if letra in ["A", "B", "C", "D"]:
                            if lt == 1:
                                novas_letras.append(alfabeto[23][1])
                            elif lt == 2:
                                novas_letras.append(alfabeto[24][1])
                            elif lt == 3:
                                novas_letras.append(alfabeto[25][1])
                            elif lt == 4:
                                novas_letras.append(alfabeto[26][1])
                        else:
                            novas_letras.append(alfabeto[lt-4][0])

                    elif letra == alfabeto[lt][1]:
                        if letra in ["a", "b", "c", "d"]:
                            if lt == 1:
                                novas_letras.append(alfabeto[23][1])
                            elif lt == 2:
                                novas_letras.append(alfabeto[24][1])
                            elif lt == 3:
                                novas_letras.append(alfabeto[25][1])
                            elif lt == 4:
                                novas_letras.append(alfabeto[26][1])
                        else:
                            novas_letras.append(alfabeto[lt-4][1])
                    else:
                        vl = letra

                if vl in acentos_maiusculos or vl in acentos_minusculos or vl in especiais:
                    novas_letras.append(vl)
            novas_letras.append(" ")

        frase = separador.join(novas_letras).replace(", ", "")
        arquivo.write(frase)


if __name__ == "__main__":
    with open("log/mensagem.txt", mode="r", encoding="utf-8") as arquivo:
        carta = arquivo.read().split()
        descriptografar(carta)
