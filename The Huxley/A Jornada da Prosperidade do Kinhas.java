import java.io.*;
import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

public class HuxleyCode {
    private Integer primo(int n){
        int retorno = -1;
        try {
            for (int i = 2; i < n; i++) {
                if(n % i == 0){
                    retorno = 0;
                    break;
                }
                else{
                    retorno = 1;
                }
            }
        } catch (Exception e) {
            retorno = -1;    
        }
        if(n == 2){
            retorno = 1;
        }
        return retorno;
    }

    private int fatorial(int x){
        int r = 0;
        if(x != 0) {
            for (int calc = 1; calc <= x; calc++) {
                if(r == 0){r = 1;}
                r *= calc;
            }
        }
        return r;
    }

    private int TorreDaProsperidade(int exp){
        int moedas = 0;   
        for(int i = exp; i > 0; i--){  
            if(i % 7 == 0){ 
                moedas += 30;        
            }
        }
        return moedas;
    }

    private StringBuilder CirculoDaProsperidade(int distancia, int tamanho){
        Integer[] circulo = new Integer[tamanho];
        int contagem = 0; 
        int experiencia = 0, vale_moedas = 0, moedas = 0;
        ArrayList<String> sequencia = new ArrayList<String>();
        int condicaoFinal = 0;
        for(; distancia > 0; distancia--){
            if(contagem == circulo.length){
                contagem = 0;
            }
            if(primo(contagem) == 1){
                experiencia += contagem;  
                sequencia.add("" + contagem);    
            }
            if(contagem == 7){
                vale_moedas++;
            }
            contagem++;
        }
        moedas = fatorial(vale_moedas);
        int multiplosDeSete = 0;
        int desistir = 0;
        if(moedas == 0){
            moedas = TorreDaProsperidade(experiencia);
            multiplosDeSete = moedas/30;
            condicaoFinal = 1;
            if(moedas == 0){
                desistir = 1;
            }
        }
        StringBuilder primos = new StringBuilder(new String(""));
        for(String s:sequencia){
            primos.append(s);
            primos.append(" ");
        }
        primos.append("\n");
        String strExpMoedas = "Experiencia = " + experiencia + " Moedas = " + moedas;
        String strNaoMeodas = "Ja que nao achei moedas, vou na Torre\n";
        StringBuilder multSete = new StringBuilder("");

        if(multiplosDeSete != 0) {  
            for (int k = 1; k <= multiplosDeSete; k++) {

                if(k == multiplosDeSete){
                    multSete.append(k*7);
                    multSete.append(" \n");
                }
                else{
                    multSete.append(k*7);
                    multSete.append(" ");
                }
            }
        }
        else{
            multSete.append(0);
        }

        String fraseFinal; 
        if(desistir == 1){
            fraseFinal = "Desisto.\n";
        }
        else{
            fraseFinal = "Consegui " + moedas + " moedas na Torre";
        }

        StringBuilder retorno = new StringBuilder("");
        if(condicaoFinal == 0){ 
            retorno.append(primos);
            retorno.append(strExpMoedas);
        }
        else if(desistir == 1){ 
            retorno.append(primos);
            strExpMoedas = "Experiencia = " + experiencia + " Moedas = 0\n";
            retorno.append(strExpMoedas);
            retorno.append(strNaoMeodas);
            retorno.append(fraseFinal);
        }
        else{
            retorno.append(primos);
            strExpMoedas = "Experiencia = " + experiencia + " Moedas = 0\n";
            retorno.append(strExpMoedas);
            retorno.append(strNaoMeodas);
            retorno.append(multSete);
            retorno.append(fraseFinal);
        }

        return retorno;
    }

    public static void main(String[] args) {
        HuxleyCode func = new HuxleyCode();
        Scanner scanner = new Scanner(System.in);

        int dis, tam;

        String leitura = scanner.nextLine();
        String[] valores = leitura.split("\\s");
        dis = Integer.parseInt(valores[0]); 
        tam = Integer.parseInt(valores[1]);  

        System.out.println(func.CirculoDaProsperidade(dis, tam));
    }
}