/*
1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
R: Não consegui desenvolver uma solução lógica para esste desafio!
*/

/*
2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.

OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
*/

import java.util.*;

public class Main {
    public static void main(String[] args) {

        // 2) Não consegui progredir no exercício
        ArrayList<Double> lista= new ArrayList<Double>();
        
        // Com somente 1 for dá esse erro: (Main.java:15: error: integer number too large: 99999999999999999999999999)
        
        for(double j=0; j < 99999999999999999999999999; j++) {
            lista.add(j); 
        }
         
        System.out.println(lista);
    }
}