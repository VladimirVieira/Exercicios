package fundamentos;

import java.util.Scanner;

/*
 * Escreva um programa que leia um valor em metros e o exiba
 * convertido em centimetros e milimetros
 */
public class Desafio008 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite um valor em metros:");
		float metros = scanner.nextFloat();
		System.out.println("Valor em centimetros:" + metros * 100);
		System.out.println("Valor em milimetros:" + metros * 1000);
		scanner.close();
	}
}
