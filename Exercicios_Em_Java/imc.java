import java.util.Scanner;
public class imc{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		System.out.println("Digite a sua altura:");
		double altura = scanner.nextDouble();
		scanner.nextLine();		
		System.out.println("Digite o seu peso:");	
		double peso = scanner.nextDouble();
		double imc = peso/(altura*altura);
		System.out.printf("O seu imc é:%f",imc);
	}
}
