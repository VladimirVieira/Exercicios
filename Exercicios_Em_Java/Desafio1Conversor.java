import java.util.Scanner;

public class Desafio1Conversor {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		double farenheit = scanner.nextDouble();
		
		double celsius = (farenheit - 32)*5/9.0;
		
		System.out.printf("A conversão resultou em:%.2f°\n", celsius);
		
		scanner.close();
		
	}

}
