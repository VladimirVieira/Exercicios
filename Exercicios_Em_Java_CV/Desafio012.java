package fundamentos;

import java.util.Scanner;

/*
 * Faça um algoritmo que leia o preço de um produto e mostre seu
 * novo preco com 5% de desconto
 */
public class Desafio012 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		float preco = scanner.nextFloat();
		scanner.nextLine();
		System.out.printf("Preco do produto:R$ %.2f", preco);
		System.out.println();
		System.out.printf("Novo preco:R$%.2f", preco*0.95);
		scanner.close();
	}

}
