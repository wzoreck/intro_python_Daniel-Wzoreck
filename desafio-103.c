/*
DESAFIO!!!
Implemente um algoritmo para inverter a ordem de uma string em sua
linguagem de programacao favorita. Nao use funcoes/metodos prontos.
*/

#include <stdio.h>

int main() {

    char v[30];
    int i, cont=0;

    printf("Entrada: ");
    fgets(v, 30, stdin);

    for(i=0; i<30; i++){
        if(v[i] != '\n'){
            cont++;
        } else{
            break;
        }
    }
    char v2[cont];

    // Invertendo a string
    int j=0;
    for(i=cont-1; i>=0; i--){
        v2[i]= v[j];
        j++;
    }
    v2[cont]= '\n';
    v2[cont+1]= '\0';

    printf("Saída:");
    printf("%s", v2);

    return 0;
}