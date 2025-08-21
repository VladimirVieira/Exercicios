import java.util.Scanner;
public class Desafio13{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        int maior = 0;
        for(int i = 0;i<10;i++){
            int num = scanner.nextInt();
            scanner.nextLine();
            if(i==0){
                maior = num;
            }else if(maior<num){
                maior = num;
            }
        }
        System.out.println(maior);
        scanner.close();

    }   
}

