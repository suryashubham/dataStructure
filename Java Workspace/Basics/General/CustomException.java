import java.util.Scanner;

class UnderAgeToVoteException extends Exception{
		UnderAgeToVoteException(){

		}

		UnderAgeToVoteException(String userMessage){
			super(userMessage);
		}
}


//Method 1

/*public class CustomException{
	public static void main(String[] args) throws UnderAgeToVoteException {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter an age to check the eligiblity of the voter:");
		int age = s.nextInt();
		if(age<18){
			//throw an exception
			int req = 18-age;
			throw new UnderAgeToVoteException("Please wait for another" + " " + req +"yrs.");
		}
		else{
			System.out.println("You're eligible to vote.");
		}
	}

}*/

//Method 2 --- Recommended to use try-catch

public class CustomException extends UnderAgeToVoteException{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter an age to check the eligiblity of the voter:");
		int age = s.nextInt();

		try{
			if(age<18){
				int req = 18-age;
				throw new UnderAgeToVoteException("Please wait for another" + " " + req +"yrs.");
			}
		}

		catch(UnderAgeToVoteException ex){
			System.out.println(ex.getMessage());
		}
	}
}