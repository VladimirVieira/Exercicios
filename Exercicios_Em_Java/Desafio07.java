/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;
public class Desafio07
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
		int numero = -1;
		
		do{
		    System.out.println("Digite um número inteiro:");
		    numero = scanner.nextInt();
		    scanner.nextLine();
		    if(numero!=0){
		        continue;
		    }
		}while(numero<0 || numero>11);
		
		scanner.close();
	}
}