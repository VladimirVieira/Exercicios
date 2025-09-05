package fundamentos;

import java.util.Scanner;

/**
 * Faça um programa que leia algo pelo teclado e mostre na tela o seu
 * tipo primitivo e todas as informações possíveis sobre ele
 */
public class Desafio004 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String algo = scanner.nextLine();
		System.out.println("é vazio:" + algo.isBlank());
		boolean isSpace = algo.chars().allMatch(Character::isWhitespace);
		boolean isNumeric = algo.chars().allMatch(Character::isDigit);
		boolean isAlpha = algo.chars().allMatch(Character::isLetter);
		boolean isAlnum = algo.chars().allMatch(Character::isLetterOrDigit);
		boolean isUpper = algo.equals(algo.toUpperCase()) && !algo.isEmpty();
		boolean isLower = algo.equals(algo.toLowerCase()) && !algo.isEmpty();
		
		System.out.println(isSpace);
		System.out.println(isNumeric);
		System.out.println(isAlpha);
		System.out.println(isAlnum);
		System.out.println(isUpper);
		System.out.println(isLower);
		
		scanner.close();
	}
}
