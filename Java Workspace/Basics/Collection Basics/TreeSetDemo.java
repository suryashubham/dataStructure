import java.util.*;

/*
   We need to implement Comparable Interface Since we're adding 
 * Employee Objects in TreeSet and If the Employee class is not implementing
 * Comaprable Interface then ClassCastException will be thrown.
 * 
 */
class Employee implements Comparable{
	String name;
	int eid;

	Employee(String name, int eid){
		this.name = name;
		this.eid = eid;
	}

	public String toString(){
		return name + "--" + eid; 
	}

	public int compareTo(Object obj){
		Employee e = (Employee)obj;
		int eid_1 = this.eid;
		int eid_2 = e.eid;
        //Default Natural sorting Order
		if(eid_1<eid_2) return -1;
		else if(eid_1>eid_2) return 1;
		else return 0; 
	}

}

public class TreeSetDemo{
	public static void main(String[] args) {
		Employee e1 = new Employee("surya",10);
		Employee e2 = new Employee("shubham",20);
		Employee e3 = new Employee("kumar",30);
		TreeSet t = new TreeSet();
		t.add(e1);
		t.add(e2);
		t.add(e3);
		System.out.println(t);

		TreeSet t1 = new TreeSet(new MyComparator());
		t1.add(e1);
		t1.add(e2);
		t1.add(e3);
		System.out.println(t1);
	}
}

//customised sorting based on name not eid.
class MyComparator implements Comparator{
	public int compare(Object obj1, Object obj2){
		Employee e1 = (Employee)obj1;
		Employee e2 = (Employee)obj2;
		String s1 = e1.name;
		String s2 = e2.name;
		return s1.compareTo(s2);
	}
}