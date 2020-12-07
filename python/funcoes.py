from random import randint


def letra_numero(frase): #converte as letras em números segundo a convenção do algortimo e retorna um array com estes
    frasen = []

    for i in range(0, len(frase)):
        if frase[i] == "a":
            frasen.append(2) 
        elif frase[i] == "b":
            frasen.append(3)
        elif frase[i] == "c":
            frasen.append(4)
        elif frase[i] == "d":
            frasen.append(5)
        elif frase[i] == "e":
            frasen.append(6)
        elif frase[i] == "f":
            frasen.append(7)
        elif frase[i] == "g":
            frasen.append(8)
        elif frase[i] == "h":
            frasen.append(9)
        elif frase[i] == "i":
            frasen.append(10)
        elif frase[i] == "j":
            frasen.append(11)
        elif frase[i] == "k":
            frasen.append(12)
        elif frase[i] == "l":
            frasen.append(13)
        elif frase[i] == "m":
            frasen.append(14)
        elif frase[i] == "n":
            frasen.append(15)
        elif frase[i] == "o":
            frasen.append(16)
        elif frase[i] == "p":
            frasen.append(17)
        elif frase[i] == "q":
            frasen.append(18)
        elif frase[i] == "r":
            frasen.append(19)
        elif frase[i] == "s":
            frasen.append(20)
        elif frase[i] == "t":
            frasen.append(21)
        elif frase[i] == "u":
            frasen.append(22)
        elif frase[i] == "v":
            frasen.append(23)
        elif frase[i] == "w":
            frasen.append(24)
        elif frase[i] == "x":
            frasen.append(25)
        elif frase[i] == "y":
            frasen.append(26)
        elif frase[i] == "z":
            frasen.append(27)
        elif frase[i] == " ":
            frasen.append(28)
    return frasen


def numero_letra(numeros): #converte o o número em letra segundo a convenção do algoritmo
    convertido = []
    for i in range(0, len(numeros)):
        if numeros[i] == 2:
            convertido.append("a") 
        elif numeros[i] == 3:
            convertido.append("b")
        elif numeros[i] == 4:
            convertido.append("c")
        elif numeros[i] == 5:
            convertido.append("d")
        elif numeros[i] == 6:
            convertido.append("e")
        elif numeros[i] == 7:
            convertido.append("f")
        elif numeros[i] == 8:
            convertido.append("g")
        elif numeros[i] == 9:
            convertido.append("h")
        elif numeros[i] == 10:
            convertido.append("i")
        elif numeros[i] == 11:
            convertido.append("j")
        elif numeros[i] == 12:
            convertido.append("k")
        elif numeros[i] == 13:
            convertido.append("l")
        elif numeros[i] == 14:
            convertido.append("m")
        elif numeros[i] == 15:
            convertido.append("n")
        elif numeros[i] == 16:
            convertido.append("o")
        elif numeros[i] == 17:
            convertido.append("p")
        elif numeros[i] == 18:
            convertido.append("q")
        elif numeros[i] == 19:
            convertido.append("r")
        elif numeros[i] == 20:
            convertido.append("s")
        elif numeros[i] == 21:
            convertido.append("t")
        elif numeros[i] == 22:
            convertido.append("u")
        elif numeros[i] == 23:
            convertido.append("v")
        elif numeros[i] == 24:
            convertido.append("w")
        elif numeros[i] == 25:
            convertido.append("x")
        elif numeros[i] == 26:
            convertido.append("y")
        elif numeros[i] == 27:
            convertido.append("z")
        elif numeros[i] == 28:
            convertido.append(" ")
    return convertido


def inverso(a, m): #calcula e retorna o inverso de a mod m
    for d in range(1, m):
        if ((d * a) % m == 1): 
            return d


def mdc(a, d): #calcula e retorna o mdc de dois números com base no Algoritmo de euclides
    resto = a % d
    if (resto == 0):
        return d
    else:
        return mdc(d, resto)


def gerar_e(totiente): #gera e retorna um valor aleatório para E
    e = randint(2, totiente) #totiente aqui funciona como o limite para a geração do número
    while (mdc(e, totiente) != 1): #se o mdc for 1, significa que eles não tem os mesmos divisores, o que satisfaz a condição
        e = randint(1, totiente)
    return e


def primo(num): #decide se um dado número é primo ou não
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    
    if cont > 2:
        return False
    else:
        return True


def gerar_chaves(): #gera as chaves, caso a opção no menu seja 1
    print("""[1] Gerar os números primos aleatoriamente
[2] Inserir os números primos""")
    opcaoprim = int(input("Sua opção: "))

    if (opcaoprim == 1): #gera primos automaticamente dentro de um intervalo
        p = randint(2, 999)
        while (not primo(p)):
            p = randint(2, 999)

        q = randint(2, 999)
        while (not primo(q) or q == p):
            q = randint(2, 999)  
    
    elif (opcaoprim == 2): #o usuário insere os números
        p = int(input("Insira o primo p: "))
        while (not primo(p)):
            p = int(input("Este número não é primo! Por favor, insira o primo p: "))
        
        q = int(input("Insira o primo q: "))
        while (not primo(q)):
            q = int(input("Este número não é primo! Por favor, insira o primo q: "))
        
    
    #agora que temos os primos P e Q, podemos encontrar n e a funcao totiente:
    print("Gerando n...")
    n = p * q
    totiente = (p - 1) * (q - 1)
    # e é um valor arbitrário entre 1 e a totiente, relativamente primo a esta     
    e = gerar_e(totiente) #temos as chaves públicas
    d = inverso(e, totiente) #para a chave privada, precisamos do inverso de e mod totiente;
    
    pub = open('chaves.txt',  'w')
    pub.write(f"Pública: [n: {n}, e: {e}]\nPrivada: [p: {p}, q: {q}, d: {d}]")
    pub.close()
    print("Chaves adicionadas ao arquivo 'chaves.txt'")


def encriptar():
    frase = str(input("Insira a frase a ser encripitada: "))
    convert = letra_numero(frase) #temos a frase pré-codificada, convertida em números
    print("Insira a chave pública (se já foi gerada, está em 'chaves.txt'): ")
    n = int(input("n: "))
    e = int(input("e: "))
    
    encrip = open('encriptada.txt', 'w')
   
    for i in range(len(convert)):
        convert[i] = ((convert[i]**e) % n) #numero elevado a E mod N: encriptando a mensagem
        if (i < len(convert)):
            if (i != len(convert)):
                encrip.write(f"{convert[i]} ")
            else:
                encrip.write(f"{convert[i]}")
    encrip.close()

    print("A mensagem encripitada foi adicionada ao arquivo 'encriptada.txt'")
    
def decriptar():
    msg = input("Insira a mensagem a ser decriptada (se já foi gerada, está em 'encriptada.txt'): ").split()
    for num in range(0, len(msg)):
        msg[num] = int(msg[num]) #de string para int
    
    print("Insira a chave privada: ")
    p = int(input('p: '))
    q = int(input('q: '))
    d = int(input("d: "))
    n = p * q

    for c in range(0, len(msg)):
        msg[c] = ((msg[c] ** d) % n) #decriptando...

    decriptada = numero_letra(msg)
    arquivo = open('decriptada.txt', 'w')
    for i in range(0, len(decriptada)):
        arquivo.write(decriptada[i])
    arquivo.close()
    
    print("A mensagem decriptada foi armazenada em 'decriptada.txt'")