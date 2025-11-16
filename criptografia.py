"""
Esse arquivo visa criar um método de criptografia arcaico utilizado por militares no passado para proteger informações
confidenciais, muitas dessas mensagens tinha conteúdo relacionados às táticas de guerra e locais de ataques. Criada por
Cesar, esse tipo de serealização de mensagem só era entendida pelo exército e demais membros do governo dele.

A lógica consiste em trocar cada letra da palavra original por 4 letras após elas, seria como uma soma onde 'A' vale 1,
'B' vale 2 e assim por diante até chegar nas últimas letras do alfabeto 'W', 'X', 'Y' e 'Z', por exemplo:

** obs: não importa se é letra maíuscula ou minúscula, o valor permanece o mesmo **

A = 1
B = 2
C = 3
D = 4
...
W = 23
X = 24
Y = 25
Z = 26

Como o deslocamento das palavras será trocada após dela a sua quarta contagem. No programa, o alfabeto será um dicionário
as chaves deste dicionário serão os números e cada número terá sua letra representada e estará contida numa lista que irá
guardar — uma letra maíuscula e uma minúscula.

As chaves serão essenciais para realizar a troca ao somar os valores de cada chave por 4:

A = 1 + 4 = E
B = 2 + 4 = F
C = 3 + 4 = G
D = 4 + 4 = H
...
V = 22 + 4 = Z
...

ATENÇÃO -> Como a soma da chave V é igual a 26 e aponta para chave Z, isso significa que todos os valores disponíveis de
soma com 4 se esgotam aqui. Portanto, as últimas letras equivalem a mesma quantidade das quatro primeiras e em virtude
disso os útimos valores serão substituídos na ordem alfabética também em ambas, o que vai acontecer na criptografia é:

W = 23 vai apontar para A = 1
X = 24 vai apontar para B = 2
Y = 25 vai apontar para C = 3
Z = 26 vai apontar para D = 4

Do mesmo modo o inverso também será verdadeiro. Com os passos aplicados ao realizar a codificação, teremos o alfabeto
cifrado e nos permitirá criar a "mensagem secreta" que queremos.

"""

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
    """
    :param: Receberá a mensagem que será criptografada
    :return: Nada será retornado na tela, porém, salvará o conteúdo criptografado no diretório log.
    """
    with open("log/mensagem_criptografada.txt", mode="w", encoding="utf-8") as arquivo:
        """
        vl -> Significa velha letra
        
        separador -> Desempenhará um papel importante, quando o programa for juntar as letras para formar a mensagem, a
        variável será utilizada para remover os espaços entre as letrs que contém ", " pois cada letra será armazenada
        numa lista chamada "novas_letras". Depois de removido os espaços entre as letras para formar as palavras, o 
        conteúdo formado será guardado na variável "frase".
        
        arquivo.write(frase) -> com a abertura do arquivo no modo escrita, será gerado um documento com as informações
        cifradas.
        """
        vl = ''
        separador = ", "
        novas_letras = []

        for palavra in carta:
            for letra in palavra:
                for i, lt in enumerate(alfabeto):
                    if letra == alfabeto[lt][0]:
                        if letra in ["W", "X", "Y", "Z"]:  # Lógica explicada nos parágrafos 37 ao 44.
                            if lt == 23:
                                novas_letras.append(alfabeto[1][0])
                            elif lt == 24:
                                novas_letras.append(alfabeto[2][0])
                            elif lt == 25:
                                novas_letras.append(alfabeto[3][0])
                            elif lt == 26:
                                novas_letras.append(alfabeto[4][0])
                        else:
                            # Caso as letras detectadas não sejam as quatro últimas, a adição será realizada para
                            # retornar uma letra do alfabeto cifrado.
                            novas_letras.append(alfabeto[lt+4][0])

                    elif letra == alfabeto[lt][1]:
                        if letra in ["w", "x", "y", "z"]:  # Lógica explicada nos parágrafos 37 ao 44.
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
                        # Caso as letras detectadas não sejam as quatro últimas, a adição será realizada para
                        # retornar uma letra do alfabeto cifrado.
                        vl = letra

                # Se a letra contiver acentos ou caracteres especiais, não será feito nenhum tipo de tratamento. Será
                # armazenado, fica a seu critério melhorar o algoritmo se preferir.
                if vl in acentos_maiusculos or vl in acentos_minusculos or vl in especiais:
                    novas_letras.append(vl)
            novas_letras.append(" ")

        # Explicação no parágrafo 94 ao 102
        frase = separador.join(novas_letras).replace(", ", "")
        arquivo.write(frase)


if __name__ == "__main__":
    with open("log/teste.txt", mode="r", encoding="utf-8") as arquivo:
        carta = arquivo.read().split()
        criptografar(carta)
