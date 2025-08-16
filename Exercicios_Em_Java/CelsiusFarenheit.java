import java.util.Scanner;

public class CelsiusFarenheit{
	public static void main(String[] args){
		Scanner entrada = new Scanner(System.in);
		
		double celsius = entrada.nextDouble();
		double farenheit = (9*celsius + 160)/5.0;
		System.out.printf("Temperatura em %.2f equivale a %.2f", celsius, farenheit);
		
		entrada.close(); 
	}
}
