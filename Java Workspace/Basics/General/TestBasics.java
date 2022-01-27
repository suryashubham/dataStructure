class TestBasics{
	String name="Surya";
	int age = 26;
	int id=123;
	int mob = 9939;

	static TestBasics t = k();
	// System.out.println(t);


	static TestBasics k(){
		return new TestBasics();
	}

	public String toString(){
		return name+age+id+mob;
	}

	void m1(String name, int age){
			this.name=name;
			this.age=age;
			System.out.println(this);
	}

	void m2(int a,int b){
		id = a;
		mob = b;
		//----Same logic-----
		// this.id=a;
		// this.mob=b;
		System.out.println(this);
	}

	public static void main(String[] args) {
		System.out.println(t);
		//TestBasics t = new TestBasics();
		// System.out.println(t.age);
		// t.m1("Shubham",27);
		// t.m2(121,8348);
	}
}