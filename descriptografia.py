"""
O arquivo de descriptografia irá realizar o processo inverso do que é proposto no arquivo de criptografia. Portanto, vai
ser subtraído 4 de cada chave que representa uma letra do alfabeto (lista) e com isso a mensagem será decifrada, exemplo:

E = 5 - 4 = A
F = 6 - 4 = B
G = 7 - 4 = C
H = 8 - 4 = D
...
W = 23 - 4 = S
X = 24 - 4 = T
Y = 25 - 4 = U
Z = 26 - 4 = V


ATENÇÃO -> Subtrair o inverso na lista irá causar erro, pois a primeira chave do dicionário começa em 1 e os valores são
naturais e limitam-se ao tamanho do alfabeto. Portanto, nessa situação, será feito o mesmo método aborado no arquivo de
cripografia onde as quatro chaves inciais do dicionário apontam para as quatro últimas.

A = 1 vai apontar para W = 23
B = 2 vai apontar para X = 24
C = 3 vai apontar para Y = 25
D = 4 vai apontar para Z = 26

Com os passos aplicados ao realizar a decodificação, teremos o alfabeto descifrado e nos permitirá visualizar a
"mensagem secreta".
"""
from criptografia import alfabeto, acentos_minusculos, acentos_maiusculos, especiais


def descriptografar(carta):
    """
    :param: Receberá a mensagem que será descriptografada
    :return: Nada será retornado na tela, porém, salvará o conteúdo descriptografado no diretório log.
    """
    with open("log/mensagem_descriptografada.txt", mode="w", encoding="utf-8") as arquivo:
        vl = ''
        separador = ", "
        novas_letras = []

        for palavra in carta:
            for letra in palavra:
                for i, lt in enumerate(alfabeto):
                    if letra == alfabeto[lt][0]:
                        if letra in ["A", "B", "C", "D"]:  # Lógica explicada nos parágrafos 16 ao 26.
                            if lt == 1:
                                novas_letras.append(alfabeto[23][1])
                            elif lt == 2:
                                novas_letras.append(alfabeto[24][1])
                            elif lt == 3:
                                novas_letras.append(alfabeto[25][1])
                            elif lt == 4:
                                novas_letras.append(alfabeto[26][1])
                        else:
                            # Caso as letras detectadas não sejam as quatro primeiras, a subtração para retornar a letra
                            # original será realizada.
                            novas_letras.append(alfabeto[lt-4][0])

                    elif letra == alfabeto[lt][1]:
                        if letra in ["a", "b", "c", "d"]:  # Lógica explicada nos parágrafos 16 ao 26.
                            if lt == 1:
                                novas_letras.append(alfabeto[23][1])
                            elif lt == 2:
                                novas_letras.append(alfabeto[24][1])
                            elif lt == 3:
                                novas_letras.append(alfabeto[25][1])
                            elif lt == 4:
                                novas_letras.append(alfabeto[26][1])
                        else:
                            # Caso as letras detectadas não sejam as quatro primeiras, a subtração para retornar a letra
                            # original será realizada.
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
