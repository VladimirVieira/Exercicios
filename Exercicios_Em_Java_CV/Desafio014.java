package fundamentos;

import java.util.Scanner;

/*
 * Escreva um programa que converta uma temperatura
 * digitada em °C e converta para °F
 */
public class Desafio014 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite a temperatura em °C:");
		float tempC = scanner.nextFloat();
		scanner.nextLine();
		System.out.printf("Nova temperatura em °F: %.2f", (tempC*9 + 160)/5);
		scanner.close();
	}

}
