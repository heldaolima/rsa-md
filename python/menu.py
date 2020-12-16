from funcoes import * #importa as funções do arquivo 'funcoes.py'

"""
EQUIPE:
    Diogo Henrique de Oliveira Cardoso
    Hélder Silva Ferreira Lima
    Thiago Henrique de Oliveira Figueiredo
    Thiago Lobo Pereira Barros
"""


opcao = ' '
print("--- CRIPTOGRAFIA RSA ---")

while (opcao != 4):
    print("""[1] GERAR CHAVE PÚBLICA
[2] ENCRIPITAR
[3] DESCRIPTAR
[4] SAIR""")
    opcao = int(input("Sua opção: "))
    while (opcao < 1 or opcao > 4):
        opcao = int(input("Opção inválida! Sua opção: "))

    if (opcao == 1):
        gerar_chaves()
        print("Fim da função 1")
        print("")

    elif (opcao == 2):
        encriptar()
        print("Fim da função 2")
        print("")

    elif (opcao == 3):
        decriptar()
        print("Fim da função 3")
        print("")

print("Fim do algoritmo")