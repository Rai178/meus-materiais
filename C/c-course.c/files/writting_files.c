#include <stdio.h>

int main()
{
    /*FILE *pF = fopen("test.txt", "a");

    // Verificar se o arquivo foi aberto com sucesso
    if (pF == NULL) {
        printf("Erro ao abrir o arquivo. \n");
        return 1; // retorna um valor diferente de 0 para indicar erro
    }

    fprintf(pF, "eduardo");

    fclose(pF);

    printf("Arquivo criado com sucesso. \n");
    */

    if (remove("test.txt") == 0)
    {
        printf("That file was deleted successfully!");
    }
    else
    {
        printf("That file was NOT deleted!");
    }
    
    return 0;
}