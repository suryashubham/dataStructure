import java.util.*;

/**
 * Underlying Data Structure is red-black tree.
 * Insertion Order is not Preserved.
 * All entries are inserted according to some sorting order
 * If we're depending on default sorting then keys should be Homogenous and Comparable.
 * Duplicate keys are not allowed, values can be duplicate.
 * */

//To implement default natural sorting just remove the "new MyComparator()" argument from TreeMap constructor.

public class TreeMapDemo{
	public static void main(String[] args) {
		TreeMap t = new TreeMap(new MyComparator()); 
		t.put("Z",65);
		t.put("A",66);
		t.put("K",67);
		System.out.println(t.entrySet());
	}
}

class MyComparator implements Comparator{
	public int compare(Object obj1, Object obj2){
		// System.out.print(obj1);
		String s1 = obj1.toString();
		String s2 = obj2.toString();
		return -s1.compareTo(s2);
	}
}