package fundamentos;

import java.util.Scanner;

/*
 * Faça um programa que leia a largura e a altura de uma parede em
 * metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
 * sabendo que cada litro de tinta, pinta uma área de 2m²
 */
public class Desafio011 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite a largura:");
		float largura = scanner.nextFloat();
		scanner.nextLine();
		System.out.println("Digite a altura:");
		float altura = scanner.nextFloat();
		scanner.nextLine();
		float area = largura * altura;
		float tinta = area/2;
		System.out.println("area total :" + area + "m²");
		System.out.println("Total de tinta :" + tinta + "litros");
		scanner.close();
	}

}
