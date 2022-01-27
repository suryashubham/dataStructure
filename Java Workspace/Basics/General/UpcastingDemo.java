class Parent{
	int x = 10;
	void m1(){
		System.out.println("Parent class m1() method");
	}
}

class Child extends Parent{
	int x = 100;
	void m1(){
		System.out.println("Child class m1() method");
	}
}


public class UpcastingDemo{
	public static void main(String[] args) {
	/**	
	 * If we create a sub class object and place it into a Super calss variable
	 * compiler will check type of reference, In this case our type is "Parent",
	 * so compiler will check in Super class Parent.
	 * If method is not available in super class COMPILER WILL GIVE AN ERROR
	 * If avilabe, compiler will bind(not execute) method to the current reference.
	 * In the execution time JVM will check the subclass memory,
	 * If method is NOT AVAILABLE in subclass, it will check in the super class,
	 * then super class method will be executed at run time.
	 * */
		Parent p = new Child();
		p.m1();
		/*In Upcasting Methods will be executed from sub class 2 super class
		but both static and non-static variables, will be executed from superClass */
		System.out.println(p.x);
	}
}