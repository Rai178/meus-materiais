#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int numero_inicial;
int numero_final;
int contagemParesInicial = 0;
int contagemParesFinal = 0;
int contagemAmbosPares = 0;
char resposta[4];

// achei mais fácil trabalhar com uma função que retorna true ou false
bool checagem()
{
    printf("Ponha o numero inicial: ");
    scanf("%d", &numero_inicial);
    getchar();

    printf("Ponha o numero final: ");
    scanf("%d", &numero_final);
    getchar();

    if (numero_inicial % 2 == 0 && numero_final % 2 == 0)
    {
        contagemParesFinal++;
        contagemParesInicial++;
        return true;
    }
    else if(numero_inicial % 2 != 0 && numero_final % 2 != 0)
    {
        return false;
    }
    else 
    {
        if(numero_inicial % 2 == 0 && numero_final % 2 != 0)
        {
        contagemParesInicial++;
        printf("Numero inicial e par e Numero final e impar.\n");
        }
        else
        {
        contagemParesFinal++;
        printf("Numero inicial e impar e numero final e par.\n");
        }
    }


    return false;
}

void usarChecagem(){
    bool resultado = checagem();

    //utilizando true e false eu posso saber quando ambos são pares, pois 
    //esse é um caso especial 
    if(resultado)
    {
        contagemAmbosPares++;
        printf("****%d e %d Sao  ambos numeros pares.****\n", numero_inicial, numero_final);
    }
}

int main()
{
    
    do
    {
    usarChecagem();
    
    printf("Voce deseja continuar? (sim/nao): ");
    fgets(resposta, sizeof(resposta), stdin);
    resposta[strcspn(resposta, "\n")] = '\0'; 

    while (strcmp(resposta, "sim") != 0 && strcmp(resposta, "nao") != 0) 
    {
        printf("Resposta invalida. Por favor, responda 'sim' ou 'nao' ");
        fgets(resposta, sizeof(resposta), stdin);
        resposta[strcspn(resposta, "\n")] = '\0';
        // Limpei o buffer pois se eu colocasse uma mensagem maior que o esperado
        // "Resposta inválida", repetia mais de uma vez
        // utilizei a função fgets pois consigo solucionar problemas de estouro de buffer 
        // além de ser a tecnica correta de armazenar input de string
        int c;
        while ((c = getchar()) != '\n' && c != EOF);
        // aprendi que usamos isso para limpar o buffer, pois sem isso tambem
        // dava uns bugs
    }

    }while(strcmp(resposta, "nao") != 0);
    int resultado = contagemParesFinal + contagemParesInicial;
    
    printf("Total de iniciais pares: %d\n", contagemParesInicial );
    printf("Total de finais pares: %d\n", contagemParesFinal);
    printf("Numero totais de pares: %d\n", resultado);
    printf("Comtagem Ambos pares: %d\n", contagemAmbosPares);
    printf("Programa encerrado.\n");

    return 0;
}


