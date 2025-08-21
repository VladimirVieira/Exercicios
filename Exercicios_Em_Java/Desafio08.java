import java.util.Scanner;
public class Desafio08{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite a sua primeira nota:");
        double nota1 = scanner.nextDouble();
        scanner.nextLine();
        System.out.println("Digite a sua primeira nota:");
        double nota2 = scanner.nextDouble();
        scanner.nextLine();
        
        double media = (nota1 + nota2)/2;
        System.out.printf("O aluno com média %.2f está:", media);
        
        if(media>=7){
            System.out.println("Aprovado");
        }else if(media>=4){
            System.out.println("Recuperação");
        }else{
            System.out.println("Reprovado");
        }
        scanner.close();
    }
}
