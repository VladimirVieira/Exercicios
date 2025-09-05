package fundamentos;

import java.util.Scanner;

/*
 * Crie um algoritmo que leia um número e mostre:dobro,triplo e raiz
 */
public class Desafio006 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num1 = scanner.nextInt();
		System.out.printf("Dobro:%s, triplo:%s, raiz:%s",num1*2,num1*3,Math.sqrt(num1));
		System.out.printf("Dobro:%s, triplo:%s, raiz:%s",num1*2,num1*3,Math.pow(num1,1.0/2.0));

		scanner.close();
	}

}
