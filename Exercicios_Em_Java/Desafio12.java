import java.util.Scanner;

public class Desafio12{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in); 
        int somatorio = 0;
        while(true){
            int num = scanner.nextInt();
            scanner.nextLine();
            if(num>-1){
                somatorio+=num;
                System.out.println("Valor do somatorio:" + somatorio);
            }else{
                break;
            }
        }

    }
    
}

