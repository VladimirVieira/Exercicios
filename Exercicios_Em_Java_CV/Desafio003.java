package fundamentos;

import java.util.Scanner;
//Crie um programa que leia dois números e mostre a soma entre eles
public class Desafio003 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite o primeiro valor:");
		int valor1 = scanner.nextInt();
		scanner.nextLine();
		System.out.print("Digite o segundo valor:");
		int valor2 = scanner.nextInt();
		scanner.nextLine();
		System.out.printf("%s + %s = %s", valor1, valor2, valor1+valor2);
	
		scanner.close();
	}

}
