import java.util.Scanner;
public class Desafio09{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um n�mero inteiro:"); 
        int numero = scanner.nextInt();
        int cont = 0;
        
        for(int i = 1;i<=numero;i++){
            if (numero%i==0){
                cont++;
            }
        }
        
        if(cont==2){
            System.out.printf("O n�mero %d � primo", numero);
        }

    }
}
