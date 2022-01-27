import java.util.Scanner;

class UserInput{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter One sentence");
		String sn = s.nextLine();
		System.out.println(sn);

		System.out.println("Enter a string value:");
		String st = s.next();
		System.out.println(st);

		System.out.println("Enter a Integer value:");
		int i = s.nextInt();
		System.out.println(i);

		System.out.println("Enter a Boolean value:");
		boolean b = s.nextBoolean();
		System.out.println(b);

		System.out.println("Enter a Float value:");
		float f = s.nextFloat();
		System.out.println(f);


	}
}