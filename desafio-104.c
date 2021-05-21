/*
DESAFIO!!!
1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
2) Agora faca sem utilizar uma terceira variavel temporaria.
OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
*/

#include <stdio.h>

int main() {

    int x, y, temp;

    printf("Informe um valor para X: ");
    scanf("%d", &x);
    printf("Informe um valor para Y: ");
    scanf("%d", &y);

    // 1) Invertendo
    temp = x;
    x = y;
    y = temp;

    printf("\n\nValores invertidos");
    printf("\nO valor de X é: %d", x);
    printf("\nO valor de Y é: %d", y);

    // Desinvertendo os valores
    temp = x;
    x = y;
    y = temp;

    printf("\n\nValores em suas posições originais");
    printf("\nO valor de X é: %d", x);
    printf("\nO valor de Y é: %d", y);

    // 2) Invertendo sem utilizar variaveis adicionais
    // Usando truque com o XOR

    x ^= y;
    y ^= x;
    x ^= y;

    printf("\n\nValores invertidos");
    printf("\nO valor de X é: %d", x);
    printf("\nO valor de Y é: %d", y);

    return 0;
}

/*
Mas para entender melhor vamos trabalhar com exemplos.
Suponha que x seja igual a 10 e y igual a 7.
Como visto acima o XOR trabalha a nível de bit, portanto
o que ele irá analisar será:

x = 1010;
y = 0111;

Pois 1010 em decimal é igual a 10 e 0111 é igual a 7.
Então, na primeira linha, a operação de ou exclusivo será
executada da seguinte forma:

x -> 1010
y -> 0111
---------
x =  1101

Esse será o novo valor para x. A segunda linha executa a mesma
operação de ou exclusivo, porém com o novo valor de x e agora
atribuindo o resultado na variável y. Ao analisar o novo valor
de y, vemos que o número binário 1010 convertido para decimal
é 10, e 10 é o valor original da variável x.
Ou seja, já colocamos o valor de x em y!

x -> 1101
y -> 0111
---------
y =  1010

E por fim, x irá receber novamente o valor do XOR e desta vez
tanto x quanto y possuem valores diferentes dos originais.

x -> 1101
y -> 1010
---------
x =  0111

Nesta ultima etapa x recebeu o valor original de y
como resultado do XOR.

FONTE: https://sonoscompiuter.wordpress.com/2016/08/28/utilizando-o-operador-xor-em-c/
*/