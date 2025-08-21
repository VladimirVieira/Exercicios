import java.util.Scanner;
import java.util.Random;
public class Desafio11{
    public static void main(String[] args){
        Random random = new Random();
        int cont = 0;
        int numero = random.nextInt(100);
        Scanner scanner = new Scanner(System.in);
        
        while(cont<10){
            int num = scanner.nextInt();
            scanner.nextLine();
            
            if(num == numero){
                System.out.println("Você acertou");
                break;
            }
            cont++;
        }
        System.out.println(numero);
        scanner.close();

    }   
}

