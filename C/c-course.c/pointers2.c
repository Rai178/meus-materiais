#include <stdio.h>

int main() {
    int var = 10;  // Uma variável inteira
    int *ptr; // Declaração de um ponteiro para inteiro

    ptr = &var; // armazena o endereço de 'var' no ponteiro 'ptr'

    // acessando o valor e o endereço
    printf("valor de var: %d\n", var);  // imprime o valor de 'var'
    printf("Endereco de var: %p\n", &var); //imprime o endereço de 'var'

    // usando o ponteiro para acessar o valor e o endereço
    printf("Endereco armazenado no ponteiro ptr: %p\n", ptr); 
    //imprime o endereço que 'ptr' armazena (que é o de 'var')
    printf("Valor apontado por ptr: %d\n", *ptr); 
    //usa a indireção para acessar o valor armazenado no endereço
}