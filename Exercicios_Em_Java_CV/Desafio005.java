package fundamentos;

import java.util.Scanner;

/**
 * Faça um programa que leia um número inteiro e mostre na tela o seu
 * sucessor e seu antecessor
 */
public class Desafio005 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num1 = scanner.nextInt();
		System.out.printf("O sucessor %s e o antecessor %s", num1+1, num1-1);
		scanner.close();
	}

}
