package fundamentos;

import java.util.Scanner;

/*
 * Crie um programa que leia quanto dinheiro uma pessoa tem na
 * carteira e mostre quantos dolares ela pode comprar
 */
public class Desafio010 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Quanto você possui em sua carteira:R$");
		float dinheiro = scanner.nextFloat();
		System.out.printf("O valor R$%s permite comprar U$%.2f", dinheiro, dinheiro/3.27);
		
		scanner.close();
	}

}
