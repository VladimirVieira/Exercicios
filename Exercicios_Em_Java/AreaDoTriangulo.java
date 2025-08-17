import java.util.Scanner;

public class AreaDoTriangulo{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite o tamanho da base do triangulo:");
		double base = scanner.nextDouble();
		System.out.println("Digite o tamanho da altura do triangulo:");
		double altura = scanner.nextDouble();
		System.out.printf("A áres do triangulo é:%.2f",(base*altura)/2);
		
		scanner.close();
	}
}
