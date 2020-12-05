#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//menu e cálculos
int primo(int num)
{
    int cont = 0;
    for (int i = 1; i <= num; i++)
    {
        if (num % i == 0)
        {
            cont++;
        }
    }
    if (cont > 2)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

int euclides(int a, int d) 
{
    int resto = a % d;
    if (resto == 0)
    {
        return d;
    }
    else
    {
        return euclides(d, resto);
    }
}

int inverso(int e, int totiente) // gera a chave privada d
{
    for (int i = 1; i < totiente; i++)
    {
        if ((i * e) % totiente == 1)
        {
            return i;
        }
    }
}

int gerar_e(int limite) // limite = totiente. Gera um valor arbitrário cujos divisores não são comuns ao totiente(p,q)
{
    srand(time(NULL));
    int lower = 1;
    for (int i = 2; i < limite; i++)
    {
        int num = (rand() % (limite - lower + 1)) + lower;
        if (euclides(num, limite) == 1) // se o mdc for 1, não há divisores comuns entre o numero e o totiente
        {
            return num;
        }
    }
    
}

int main()
{
    //menu
    int opcao;
    printf("--- CRIPTOGRAFIA RSA ---\n");
    printf("OPÇÕES:\n");
    printf("[1] GERAR CHAVE PÚBLICA\n");
    printf("[2] ENCRIPTAR\n");
    printf("[3] DESCRIPTAR\n");
    printf("Sua opção: ");
    scanf("%d", &opcao);
    if  (opcao == 1)
    {
        int p, q;
        printf("Insira o primo p: ");
        scanf("%d", &p);
        while (primo(p) == 0)
        {
            printf("Este número não é primo! Por favor, insira o primo p: ");
            scanf("%d", &p);
        }
        printf("Insira o primo q: ");
        scanf("%d", &q);
        while(primo(q) == 0)
        {
            printf("Este número não é primo! Por favor, insira o primo q: ");
            scanf("%d", &q);    
        }

        int n, totiente, e; // n, e = chaves públicas
        n = p * q;
        
        totiente = (p - 1) * (q - 1); 
        printf("n: %d\ntotiente: %d\n", n, totiente);
        
        e = 3;
        printf("e: %d\n", e);
        //Chaves públicas geradas
        int publica[2] = {n, e}; // é essa lista que será gravada no txt.  
        int d;
        d = inverso(e, totiente); //gerando a ultima chave privada.
        printf("%d\n", d);
        
        int privadas[3] = {p, q, d}
        
        
    }

}
