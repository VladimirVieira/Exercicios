
import java.util.Scanner;
public class Desafio10{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número inteiro:"); 
        int numero = scanner.nextInt();
        int cont = 0;
        
        for(int i = 1;i<=numero;i++){
            if (numero%i==0){
                cont++;
            }
        }
        
        switch(cont){
            case 2:
                System.out.println("O número é primo");
                break;
            default:
                System.out.println("O número não é primo");
                break;
        }

    }
}

