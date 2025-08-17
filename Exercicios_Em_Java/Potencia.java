import java.util.Scanner;
public class Potencia{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite um número inteiro:");
		double valor = scanner.nextDouble();
		System.out.printf("O quadrado de %f é: %f\n", valor, Math.pow(valor, 2));
		System.out.printf("O cubo de %f é: %f\n ", valor, Math.pow(valor,2));
	}
}

