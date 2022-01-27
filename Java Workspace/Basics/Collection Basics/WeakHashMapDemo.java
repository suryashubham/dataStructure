import java.util.*;

public class WeakHashMapDemo{
	public static void main(String[] args) {
		HashMap w = new HashMap();
		Temp t = new Temp();
		w.put(t,100);
		System.out.println(w);
		w=null;
		System.out.println(w);//output-->{}		
	}
}

class Temp{
	public String toString(){
		return "temp";
	}
}