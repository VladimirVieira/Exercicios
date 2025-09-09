package fundamentos;

import java.util.Scanner;
/**
 * Escreva um programa que pergunte a quantidade de km percorridos
 * por um carro alugado e a quantidade de dias pelos quais ele foi alugado
 * Calcule o preço a pagar, sabendo que o carro custa R$ por dia
 * e R$0.15 por km rodado
 */
public class Desafio015 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite a quantidade de km percorrido:");
		float km_percorrido = scanner.nextFloat();
		scanner.nextLine();
		System.out.println("Digite a quantidade de dias alugados:");
		int dias_alugados = scanner.nextInt();
		float pagamento_total =  (float)(km_percorrido * 0.15) + (dias_alugados*60);
		System.out.printf("Total a pagar:%.2f",pagamento_total);
		scanner.close();
		
		
	}

}
