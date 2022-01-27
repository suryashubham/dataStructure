import java.util.*;

public class QueueDemo{
	public static void main(String[] args) {
		PriorityQueue q = new PriorityQueue(new MyComprator());

		Employee e1 = new Employee("Surya",1);
		Employee e2 = new Employee("Kumar",100);
		Employee e3 = new Employee("Shubham",30);
		Employee e4 = new Employee("Sam",400);
    	Employee e5 = new Employee("Sham",1130);

		q.offer(e1);
		q.offer(e2);
		q.offer(e3);
		q.offer(e4);
		q.offer(e5);

		System.out.println(q);
	}
}

class MyComprator implements Comparator{
	public int compare(Object obj1, Object obj2){
		Employee e1 = (Employee)obj1;
		Employee e2 = (Employee)obj2;

		int eid1 = e1.eid;
		int eid2 = e2.eid;

		if(eid1>eid2) return -1;
		else if(eid1<eid2) return 1;
		else return 0;
	}
}

class Employee{
	String name;
	int eid;

	Employee(String name, int eid){
		this.name = name;
		this.eid = eid;
	}

	public String toString(){
		return name+"--"+eid;
	}
}

//Unexpected output 