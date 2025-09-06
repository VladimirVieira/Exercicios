package fundamentos;

import java.util.Scanner;

/**
 * Desenvolva um programa que leia as duas notas de um aluno,
 * calculee mostre a sua média
 */
public class Desafio007 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite a sua primeira nota:");
		float nota1 = scanner.nextFloat();
		scanner.nextLine();
		System.out.println("Digite a sua segunda nota:");
		float nota2 = scanner.nextFloat();
		scanner.nextLine();
		float media = (nota1+nota2)/2;
		System.out.printf("O aluno ficou com média:%.2f", media);
		scanner.close();
		
	}
}
