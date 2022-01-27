import java.util.*;

public class ArrayListDemo{
	public static void main(String[] args) {
		//In arg we can pass the default values of ArrayList
		ArrayList<Integer> al = new ArrayList<Integer>(Arrays.asList(101,102,103));
		Iterator al_iterator = al.iterator();

		for(int i=10;i>0;i--){
			al.add(i);
		}

		al.add(100);
		al.remove(1);
		int i = al.indexOf(1);
		System.out.println(i);
		Object o = al.get(3);
		System.out.println(al);

		//ConcurrentModificationException
		// while(al_iterator.hasNext()){
		// 		System.out.println(al_iterator.next());
		// }
	}
}