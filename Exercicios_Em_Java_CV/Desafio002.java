package fundamentos;

import java.util.Scanner;

//Faça um programa que leia o nome de uma pessoa e mostre
//uma mensagem de boas-vindas
public class Desafio002 {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite um nome:");
		String nome = scanner.nextLine();
		System.out.println("Seja bem vindo," + nome);
		scanner.close();
	}
}
