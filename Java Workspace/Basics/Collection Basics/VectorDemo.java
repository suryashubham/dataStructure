import java.util.*;

public class VectorDemo{
	public static void main(String[] args) {
		Vector v = new Vector();
		System.out.println(v.capacity());
		for(int i=0;i<10;i++){
			v.add(i);
		}
		System.out.println(v.capacity());
		//After exceeding initial cap of 10, if we add element spave will grow by initialCapacity*2;
		v.addElement("A");
		System.out.println(v.capacity());
	}
}