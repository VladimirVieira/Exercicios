package fundamentos;

import java.util.Scanner;

/*
 * Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
 * salário, com 15% de aumento
 */
public class Desafio013 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite o seu salario:");
		float salario = scanner.nextFloat();
		scanner.nextLine();
		System.out.printf("Salario com reajuste:R$%.2f", salario*1.15);
		scanner.close();
	}

}
